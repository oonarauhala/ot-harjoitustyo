import pygame
import sys

from entities.display_manager import DisplayManager
from entities.pet_sprite import GameSprite
from entities.pet import Pet
from entities.user_repository import UserRepository
from entities.user import User
from entities.image_loader import imageLoader


class App:
    def __init__(self):
        pygame.init()
        resolution = (450, 840)
        self.display_manager = DisplayManager(pygame.display.set_mode(resolution))
        self.image_loader = imageLoader()
        self.loaded_sprite_images = []
        self.loaded_ui_images = []
        self.current_sprite_image = 0
        # TODO ask user per info
        self.pet = Pet("Pottu", "dog")
        # TODO load user from db
        self.user = User()

    def run(self):
        # Load images
        self.loaded_ui_images = self.image_loader.load_ui_images()
        self.loaded_sprite_images = self.image_loader.load_dog_sprite_images()
        self.current_sprite_image = 0

        # Create dog sprite
        sprite = GameSprite(225, 420, self.loaded_sprite_images[0])
        sprite_group = pygame.sprite.Group()
        sprite_group.add(sprite)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    # Click sprite
                    if sprite.rect.collidepoint(position):
                        print("Woof!")
                        if self.pet.is_hungry():
                            # TODO display hunger on screen
                            self.user.feed_pet(self.pet)
                    # Click gacha button

            self.display_manager.update()
            sprite_group.draw(self.display_manager.window)
