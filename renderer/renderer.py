import pygame
from quadtree.rectangle import Rectangle
from . import settings, draw

class Renderer:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.WINDOW_NAME)

        self.resolution = settings.RESOLUTION
        self.kmPerPixel = settings.INIT_KM_PER_PIXEL
        self.focus = settings.INIT_FOCUS

        self.window = pygame.display.set_mode(self.resolution)

    def clear_screen(self):
        self.window.fill((0, 0, 0))

    def draw_all_objects(self, systemObjects, quadtree):
        draw.rect(self, (255, 255, 255), quadtree, 1)
        for sysObject in systemObjects:
            draw.circle(self, (255, 0, 100), sysObject.position, sysObject.radius)

        pygame.display.update()
