import pygame


class DisplayManager:
    def __init__(self, window):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()

    def init_window(self, resolution):
        pygame.display.set_caption("Gacha pet")
        self.window.fill((0, 0, 0))
        pygame.display.flip()

    def update(self):
        pygame.display.flip()
