import pygame

def circle(Renderer, color, pos, radius, width=0):
    objectPositionInt = point_at_scale(pos, Renderer.kmPerPixel, Renderer.resolution, Renderer.focus)
    pygame.draw.circle(Renderer.window, color, objectPositionInt, int(radius / Renderer.kmPerPixel), width)

def rect(Renderer, color, Rect, width=0):
    pos1 = point_at_scale((Rect.left, Rect.top), Renderer.kmPerPixel, Renderer.resolution, Renderer.focus)
    pos2 = point_at_scale((Rect.bottom, Rect.right), Renderer.kmPerPixel, Renderer.resolution, Renderer.focus)
    pygame.draw.rect(Renderer.window,
                     color,
                     (pos1[0], pos1[1], pos2[0], pos2[1]),
                     width,
                    )

def point_at_scale(position, kmPerPixel, resolution, focus):
    return (
        int(position[0] / kmPerPixel) + (resolution[0] // 2) - focus[0],
        int(position[1] / kmPerPixel) + (resolution[1] // 2) - focus[1]
    )