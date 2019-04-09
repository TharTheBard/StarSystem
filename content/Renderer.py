import pygame

class Renderer:
    def __init__(self, windowName, resolution):
        pygame.init()
        pygame.display.set_caption(windowName)
        self.resolution = resolution
        self.window = pygame.display.set_mode(resolution)

        self.kmPerPixel = 1500e3
        self.focus = [0, 0]

    def draw_all_objects(self, systemObjects):
        self.window.fill((0, 0, 0))

        for sysObject in systemObjects:
            #Conversion from km to pixels + pixel adjustment for camera movement
            objectPositionInt = (int(sysObject.position[0] / self.kmPerPixel) + (self.resolution[0] // 2) - self.focus[0], int(sysObject.position[1] / self.kmPerPixel) + (self.resolution[1] // 2) - self.focus[1])
            pygame.draw.circle(self.window, (255, 0, 100), objectPositionInt, int(sysObject.radius / self.kmPerPixel))

        pygame.display.update()
