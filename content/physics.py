import pygame
import math
from typing import List, Union

from content.planet import Planet, Star
from quadtree.quadtree import QuadTree
from settings import GRAVITATIONAL_CONSTANT as G


def update_positions(objects, milliseconds_passed):
    for obj in objects:
        # Conversion: km/second -> km/frame :
        frame_velocity = (
            obj.velocity[0] / milliseconds_passed, obj.velocity[1] / milliseconds_passed)
        # Update Objects' Positions for a new frame:
        obj.centre_of_mass = (
            obj.centre_of_mass[0] + frame_velocity[0], obj.centre_of_mass[1] + frame_velocity[1])


def barnes_hut_gravity(objects: List[Union[Planet, Star]], quadtree, theta):
    for obj in objects:
        if not obj.is_movable:
            continue
        obj.force = tree_force(quadtree, obj, theta)
        obj.velocity = vector_sum(obj.velocity, acceleration_from_force_mass(obj.force, obj.mass))


def tree_force(root: QuadTree, obj: Union[Star, Planet], theta: float = 1) -> tuple:
    """
    Recursively calculates gravitational force on an object *obj* in a *root* of a quadtree
    :param root:  Root of the QuadTree the object is in
    :param obj:   Object, the gravity force is being calculated for
    :param theta: Higher the theta, the faster the calculation is, but less accurate the gravity is
    :return:      Force vector for the object
    """
    r = distance(obj.centre_of_mass, root.centre_of_mass)

    if not root.divided:
        root.marked = True
        return box_force(root, obj, r)
    else:
        w = root.boundary.width
        if w/r < theta:
            root.marked = True
            return box_force(root, obj, r)
        else:
            return vector_sum(
                tree_force(root.northwest, obj, theta),
                tree_force(root.northeast, obj, theta),
                tree_force(root.southwest, obj, theta),
                tree_force(root.southeast, obj, theta),
            )


def box_force(box: QuadTree, obj: Union[Star, Planet], r: float) -> tuple:
    """
         pre_force  *  (  temp_x  ,  temp_y  )

                       █ x2 - x1     y2 - y1 █
    F = G * m1 * m2 * █ ═════════ , ═════════ █
                       █   r²          r²    █
    """
    if r == 0:
        return 0, 0

    pre_force = G * box.mass * obj.mass

    temp_x = (box.centre_of_mass[0] - obj.centre_of_mass[0]) / r**2
    temp_y = (box.centre_of_mass[1] - obj.centre_of_mass[1]) / r**2
    return pre_force * temp_x, pre_force * temp_y


def distance(first_pos: tuple, second_pos: tuple) -> float:
    if first_pos == second_pos:
        return 0
    return math.sqrt((second_pos[0] - first_pos[0]) ** 2 + (second_pos[1] - first_pos[1]) ** 2)


def n_body_centre_of_mass(*args: QuadTree) -> tuple:
    sum_mass = 0
    sum_mass_times_x = 0
    sum_mass_times_y = 0
    for point in args:
        sum_mass += point.mass
        sum_mass_times_x += point.mass * point.centre_of_mass[0]
        sum_mass_times_y += point.mass * point.centre_of_mass[1]
    try:
        return sum_mass_times_x / sum_mass, sum_mass_times_y / sum_mass
    except ZeroDivisionError:
        return sum_mass_times_x, sum_mass_times_y


def vector_sum(*args: tuple) -> tuple:
    x = 0
    y = 0
    for vector in args:
        x += vector[0]
        y += vector[1]
    return x, y


def acceleration_from_force_mass(force: tuple, mass) -> tuple:
    """
    :param force: Vector of acting force on an object
    :param mass:  Mass of an object
    :return:      Final acceleration
    """
    try:
        return force[0] / mass, force[1] / mass
    except ZeroDivisionError:
        return 0, 0
