import pygame
import random
import math
from .planet import Planet, Star
from . import physics
from renderer.renderer import Renderer
from quadtree.shapes import Rectangle, Polygon
from quadtree.quadtree import QuadTree


class StarSystem:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.renderer = Renderer()

        self.assets = {
            'objects': [],
            'quadtree': self.init_quadtree()
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

            # physics.gravity(self.assets['objects'])
            physics.barnes_hut_gravity(self.assets['objects'], self.assets['quadtree'], 2)
            physics.update_positions(self.assets['objects'], self.clock.get_time())

            self.renderer.clear_screen()
            self.renderer.draw_all_objects(self.assets)

            self.check_window_exit()
        pygame.quit()

    # def generate_test_objects(self):
        # self.assets['objects'].append(Star(100000, 35e6, (1e3, 1e3)))
        # self.assets['objects'].append(Planet(3000, 8e6, (120e6, 0), (0, -100e6)))
        # self.assets['objects'].append(Planet(50, 1.2e6, (135e6, 0), (0, -95e6)))
        # self.assets['objects'].append(Planet(2000, 6e6, (500e6, 0), (0, -20e6)))
        # self.assets['objects'].append(Planet(1500, 4e6, (300e6, 0), (0, -25e6)))
        # for i in range (150):
        #    self.assets['objects'].append(Planet(random.randint(1000, 10000), random.randint(1.2e6, 6e6), (random.randint(-6e9, 6e9), random.randint(-6e9, 6e9)), (random.randint(-39e6, 39e6), random.randint(-39e6, 39e6))))

    def generate_test_objects(self):
        self.assets['objects'].append(Star(321234, 35e6, (0, 0)))
        for i in range(30):
            self.assets['objects'].append(Star(3000, 12e6, (random.randint(-500e6, 500e6), random.randint(-500e6, 500e6))))

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

    def init_quadtree(self):
        return QuadTree(Rectangle(0, 0, 10e9, 10e9), 1)

    def refresh_quadtree(self):
        self.assets['quadtree'] = self.init_quadtree()
        for object in self.assets['objects']:
            self.assets['quadtree'].insert(object)
        self.assets['quadtree'].calc_centre_of_mass()

    def print_debug(self):
        print('______')
        # print(self.clock.get_time())
        # print(self.clock.get_rawtime())
        load = int(self.clock.get_rawtime() / 38 * 100)
        print(f"Load: {load}%")
        print(f'Focus: {self.renderer.focus}')
        print(f'kmPerPixel: {self.renderer.kmPerPixel}')
