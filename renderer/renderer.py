import pygame
import pygame.freetype
from quadtree.shapes import Rectangle
from . import settings, draw

class Renderer:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.WINDOW_NAME)
        self.font = pygame.freetype.SysFont('Arial', 15)

        self.resolution = settings.RESOLUTION
        self.kmPerPixel = settings.INIT_KM_PER_PIXEL
        self.focus = settings.INIT_FOCUS

        self.window = pygame.display.set_mode(self.resolution)
        self.show_quadtree = True

    def clear_screen(self):
        self.window.fill((0, 0, 0))

    def draw_all_objects(self, assets):
        for sysObject in assets['objects']:
            draw.circle(self, (255, 0, 100), sysObject.centre_of_mass, sysObject.radius)

        if self.show_quadtree:
            self.draw_quadtree(assets['quadtree'])

        pygame.display.update()

    def draw_quadtree(self, quadtree):
        draw.rect(self, (0, 255, 0), quadtree.boundary, 1)
        draw.text_to(self, (quadtree.boundary.x, quadtree.boundary.y), str(quadtree.mass), (0, 0, 0, 255), (0, 0, 255))

        if quadtree.divided:
            self.draw_quadtree(quadtree.northwest)
            self.draw_quadtree(quadtree.northeast)
            self.draw_quadtree(quadtree.southwest)
            self.draw_quadtree(quadtree.southeast)
