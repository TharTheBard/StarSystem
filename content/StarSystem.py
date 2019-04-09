import pygame
import random
import math
from .Renderer import Renderer
from .Planet import Planet, Star
from .Physics import Physics

class StarSystem:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.renderer = Renderer('Star System', (1024, 786))
        self.physics = Physics()
        self.objects = []

        self.add_new_object()

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(26)

            print('______')
            print(self.clock.get_time())
            print(self.clock.get_rawtime())
            print(f'Focus: {self.renderer.focus}')
            print(f'kmPerPixel: {self.renderer.kmPerPixel}')

            self.checkForKeysPressed()

            self.physics.gravity(self.objects)
            self.physics.update_positions(self.objects, self.clock.get_time())
            self.renderer.draw_all_objects(self.objects)

            self.check_window_exit()
        pygame.quit()


    def add_new_object(self):
        self.objects.append(Star(3000, 35e6, (0, 0)))
        self.objects.append(Planet(300, 5e6, (120e6, 0), (0, -39e6)))
        self.objects.append(Planet(5, 1.2e6, (135e6, 0), (0, -3e6)))
        self.objects.append(Planet(200, 6e6, (500e6, 0), (0, -20e6)))
        self.objects.append(Planet(150, 4e6, (300e6, 0), (0, -25e6)))
        #for i in range (30):
        #    self.objects.append(Planet(random.randint(150, 1000), random.randint(1.2e6, 6e6), (random.randint(-500e6, 500e6), random.randint(500e6, 500e6)), (random.randint(-39e6, 39e6), random.randint(-39e6, 39e6))))

    def checkForKeysPressed(self):
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