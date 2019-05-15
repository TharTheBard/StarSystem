import pygame

def circle(Renderer, color, pos, radius, width=0):
    objectPositionInt = point_at_scale(pos, Renderer.kmPerPixel, Renderer.resolution, Renderer.focus)
    pygame.draw.circle(Renderer.window, color, objectPositionInt, int(radius / Renderer.kmPerPixel), width)

def rect(Renderer, color, Rect, width=0):
    left_top = point_at_scale((Rect.x - Rect.half_width, Rect.y - Rect.half_height), Renderer.kmPerPixel, Renderer.resolution, Renderer.focus)
    pygame.draw.rect(Renderer.window,
                     color,
                     (left_top[0], left_top[1], Rect.width / Renderer.kmPerPixel, Rect.height / Renderer.kmPerPixel),
                     width,
                    )

def polygon(Renderer, color, pointlist, width=0):
    scaled_points = []
    for point in pointlist:
        scaled_points.append(point_at_scale(point, Renderer.kmPerPixel, Renderer.resolution, Renderer.focus))

    pygame.draw.polygon(Renderer.window, color, scaled_points, width)

def point_at_scale(position, kmPerPixel, resolution, focus):
    return (
        int(position[0] / kmPerPixel) + (resolution[0] // 2) - focus[0],
        int(position[1] / kmPerPixel) + (resolution[1] // 2) - focus[1],
    )
