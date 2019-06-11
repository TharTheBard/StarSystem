import pygame
import random


def circle(renderer, color, pos, radius, width=0):
    object_position_int = point_at_scale(pos, renderer.kmPerPixel, renderer.resolution, renderer.focus)
    pygame.draw.circle(renderer.window, color, object_position_int, int(radius / renderer.kmPerPixel), width)


def rect(renderer, color, Rect, width=0):
    left_top = point_at_scale((Rect.x - Rect.half_width, Rect.y - Rect.half_height), renderer.kmPerPixel, renderer.resolution, renderer.focus)
    pygame.draw.rect(renderer.window,
                     color,
                     (left_top[0], left_top[1], Rect.width / renderer.kmPerPixel, Rect.height / renderer.kmPerPixel),
                     width,
                     )


def polygon(renderer, color, pointlist, width=0):
    scaled_points = []
    for point in pointlist:
        scaled_points.append(point_at_scale(point, renderer.kmPerPixel, renderer.resolution, renderer.focus))

    pygame.draw.polygon(renderer.window, color, scaled_points, width)


def point_at_scale(position, kmPerPixel, resolution, focus):
    return (
        int(position[0] / kmPerPixel) + (resolution[0] // 2) - focus[0],
        int(position[1] / kmPerPixel) + (resolution[1] // 2) - focus[1],
    )


def text_to(renderer, dest, text, fgcolor=None, bgcolor=None):
    renderer.font.render_to(renderer.window, point_at_scale(dest, renderer.kmPerPixel, renderer.resolution, renderer.focus), text, fgcolor, bgcolor)


def rand_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )