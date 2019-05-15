import pygame
import random
import math
from .planet import Planet, Star
from .physics import Physics
from renderer.renderer import Renderer
from quadtree.shapes import Rectangle, Polygon
from quadtree.quadtree import QuadTree


class StarSystem:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.renderer = Renderer()
        self.physics = Physics()

        self.assets = {
            'objects': [],
            'quadtree': QuadTree(Rectangle(0, 0, 1.1e9, 1.1e9), 1)
        }

        self.generate_test_objects()

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(26)


            # self.counter += 1
            # if self.counter % 20 == 0:
            #     self.assets['objects'].append(
            #         Star(3000, 8e6, (random.randint(-500e6, 500e6), random.randint(-500e6, 500e6))))


            self.print_debug()

            self.check_for_keys_pressed()

            self.refresh_quadtree()

            self.physics.gravity(self.assets['objects'])
            self.physics.update_positions(self.assets['objects'], self.clock.get_time())

            self.renderer.clear_screen()
            self.renderer.draw_all_objects(self.assets)

            self.check_window_exit()
        pygame.quit()

    def generate_test_objects(self):
        self.assets['objects'].append(Star(3000, 35e6, (0, 0)))
        self.assets['objects'].append(Planet(300, 5e6, (120e6, 0), (0, -39e6)))
        self.assets['objects'].append(Planet(5, 1.2e6, (135e6, 0), (0, -3e6)))
        self.assets['objects'].append(Planet(200, 6e6, (500e6, 0), (0, -20e6)))
        self.assets['objects'].append(Planet(150, 4e6, (300e6, 0), (0, -25e6)))
        for i in range (30):
           self.assets['objects'].append(Planet(random.randint(150, 500), random.randint(1.2e6, 6e6), (random.randint(-500e6, 500e6), random.randint(-500e6, 500e6)), (random.randint(-39e6, 39e6), random.randint(-39e6, 39e6))))

    # def add_new_object(self):
    #     self.assets['objects'].append(Star(3000, 35e6, (0, 0)))
    #     for i in range(5):
    #         self.assets['objects'].append(Star(3000, 15e6, (random.randint(-500e6, 500e6), random.randint(-500e6, 500e6))))

    def check_for_keys_pressed(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.renderer.focus[0] -= 10
        if keys[pygame.K_RIGHT]:
            self.renderer.focus[0] += 10
        if keys[pygame.K_UP]:
            self.renderer.focus[1] -= 10
        if keys[pygame.K_DOWN]:
            self.renderer.focus[1] += 10
        if keys[pygame.K_KP_MINUS]:
            self.renderer.kmPerPixel += 10000
        if keys[pygame.K_KP_PLUS] and self.renderer.kmPerPixel > 10000:
            self.renderer.kmPerPixel -= 10000
        if keys[pygame.K_ESCAPE]:
            self.running = False

    def check_window_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def refresh_quadtree(self):
        self.assets['quadtree'] = QuadTree(Rectangle(0, 0, 1.1e9, 1.1e9), 1)
        for object in self.assets['objects']:
            self.assets['quadtree'].insert(object)

    def print_debug(self):
        print('______')
        # print(self.clock.get_time())
        # print(self.clock.get_rawtime())
        load = int(self.clock.get_rawtime() / 38 * 100)
        print(f"Load: {load}%")
        print(f'Focus: {self.renderer.focus}')
        print(f'kmPerPixel: {self.renderer.kmPerPixel}')
