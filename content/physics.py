import pygame
import math
import numpy

from content.planet import CelestialBody


def update_positions(objects, millisecondsPassed):
    for sysObject in objects:
        # Conversion: km/second -> km/frame :
        frameVelocityVector = (
        sysObject.velocityVector[0] / millisecondsPassed, sysObject.velocityVector[1] / millisecondsPassed)
        # Update Objects' Positions for a new frame:
        sysObject.centre_of_mass = (
        sysObject.centre_of_mass[0] + frameVelocityVector[0], sysObject.centre_of_mass[1] + frameVelocityVector[1])

def barnes_hut_gravity(objects, quadtree, theta):
    for current_object in objects:
        if not current_object.isMovable:
            continue
        bh_object_velocity_update(current_object, quadtree, theta)

def bh_object_velocity_update(current_object, quadtree, theta):
    if quadtree.boundary.width / distance(current_object.centre_of_mass, (quadtree.boundary.x, quadtree.boundary.y)) < theta or quadtree.northwest == None:
        grav_acc = get_grav_acc_to_object(current_object, quadtree)
        pull_vector = construct_pull_vector(current_object, quadtree, grav_acc)
        adjust_velocity_vector(current_object, pull_vector)
    else:
        bh_object_velocity_update(current_object, quadtree.northwest, theta)
        bh_object_velocity_update(current_object, quadtree.northeast, theta)
        bh_object_velocity_update(current_object, quadtree.southwest, theta)
        bh_object_velocity_update(current_object, quadtree.southeast, theta)

def gravity(objects):
    for sysObject in objects:
        object_velocity_update(sysObject, objects)

def object_velocity_update(currentObject, objects):
    for sysObject in objects:
        if currentObject == sysObject:
            continue
        gravAcc = get_grav_acc_to_object(currentObject, sysObject)
        pullVector = construct_pull_vector(currentObject, sysObject, gravAcc)
        adjust_velocity_vector(currentObject, pullVector)

def get_grav_acc_to_object(pulledObject, quadtree):
    G = 30e18
    mass = quadtree.mass
    r = distance(pulledObject.centre_of_mass, (quadtree.boundary.x, quadtree.boundary.y))

    return G * (mass / r ** 2)

def adjust_velocity_vector(pulledObject, pullVector):
    pulledObject.velocityVector = (
    pulledObject.velocityVector[0] + pullVector[0], pulledObject.velocityVector[1] + pullVector[1])

def construct_pull_vector(pulledObject, pullingObject, gravAcc):
    x = pullingObject.centre_of_mass[0] - pulledObject.centre_of_mass[0]
    y = pullingObject.centre_of_mass[1] - pulledObject.centre_of_mass[1]
    if x == 0:
        alphaRad = 1.5707963268
    else:
        alphaRad = math.atan(abs(y) / abs(x))

    aSign = numpy.sign(x)
    bSign = numpy.sign(y)

    a = math.cos(alphaRad) * gravAcc
    b = math.sin(alphaRad) * gravAcc

    return (a * aSign, b * bSign)

def distance(first_pos, second_pos):
    return math.sqrt((second_pos[0] - first_pos[0]) ** 2 + (second_pos[1] - first_pos[1]) ** 2)

def n_body_centre_of_mass(*args):
    sum_mass = 0
    sum_mass_times_x = 0
    sum_mass_times_y = 0
    for point in args:
        sum_mass += point.mass
        sum_mass_times_x += point.mass * point.centre_of_mass[0]
        sum_mass_times_y += point.mass * point.centre_of_mass[1]

    return (sum_mass_times_x / sum_mass, sum_mass_times_y / sum_mass)
