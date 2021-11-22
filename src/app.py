import pygame
import sys
from entities.pet import Pet


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Gacha pet")
        resolution = (450, 840)
        self.window = pygame.display.set_mode(resolution)
        self.dog_images = ["src/media/dog1.png"]
        self.images = []
        self.current_image = 0
        pygame.display.flip()
        self.pet = Pet("Pottu", "dog")

    def run(self):
        # Init window
        self.window.fill((0, 0, 0))
        pygame.display.flip()

        # Load images
        self.load_images(self.dog_images)
        self.window.blit(self.images[0], (110, 260))
        self.current_image = 0
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    rect = self.images[self.current_image].get_rect()
                    if rect.collidepoint(position):
                        print("Woof!")

    def load_images(self, images: list):
        for url in images:
            self.images.append(pygame.image.load(url))
