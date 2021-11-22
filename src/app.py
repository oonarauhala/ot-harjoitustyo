import pygame
import sys

from entities.display_manager import DisplayManager
from entities.pet_sprite import PetSprite
from entities.pet import Pet


class App:
    def __init__(self):
        pygame.init()
        resolution = (450, 840)
        self.display_manager = DisplayManager(pygame.display.set_mode(resolution))
        self.dog_images = ["src/media/dog1.png"]
        self.images = []
        self.current_image = 0
        self.pet = Pet("Pottu", "dog")

    def run(self):
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
            self.display_manager.update()
            sprite_group.draw(self.display_manager.window)

    def load_images(self, images: list):
        for url in images:
            self.images.append(pygame.image.load(url))
