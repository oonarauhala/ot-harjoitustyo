import pygame
import sys

from entities.pet_sprite import PetSprite
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
        self.pet = Pet("Pottu", "dog")

    def run(self):
        # Init window
        self.window.fill((0, 0, 0))
        pygame.display.flip()

        # Load images
        self.load_images(self.dog_images)
        self.current_image = 0

        # Create sprite
        image = self.images[0]
        sprite = PetSprite(225, 420, image)
        sprite_group = pygame.sprite.Group()
        sprite_group.add(sprite)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    if sprite.rect.collidepoint(position):
                        print("Woof!")
            pygame.display.flip()
            sprite_group.draw(self.window)

    def load_images(self, images: list):
        for url in images:
            self.images.append(pygame.image.load(url))
