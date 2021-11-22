import pygame
import sys
from entities.window_manager import WindowManager


class App:
    def __init__(self):
        pygame.init()
        resolution = (640, 480)
        window = pygame.display.set_mode(resolution)
        self.window_manager = WindowManager(window)
        pygame.display.flip()

    def run(self):
        # Init window
        self.window_manager.fill((0, 0, 0))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
