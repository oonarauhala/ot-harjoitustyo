import sys
import pygame
from entities.display_manager import DisplayManager
from entities.pet import Pet
from entities.user import User
from entities.image_loader import ImageLoader


class App:
    def __init__(self):
        pygame.init()
        resolution = (450, 840)
        self.display_manager = DisplayManager(
            pygame.display.set_mode(resolution), ImageLoader()
        )
        self.current_sprite_image = 0
        self.ui_sprites = []
        self.pet_sprites = []
        self.pet = Pet("Pottu", "dog")
        self.user = User()

    def run(self):
        self.initialise_game()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = event.pos
                    # Click sprite
                    if self.pet_sprites[0].rect.collidepoint(position):
                        print("Woof!")
                        if self.pet.is_hungry():
                            self.feed_pet()
                    # Click gacha button
                    if self.ui_sprites[0].rect.collidepoint(position):
                        print("Toimii")

    def initialise_game(self):
        self.current_sprite_image = 0
        self.ui_sprites = self.display_manager.create_ui_sprites()
        self.pet_sprites = self.display_manager.create_pet_sprites()
        self.display_manager.display_hunger(self.pet.hunger)

    def feed_pet(self):
        self.user.feed_pet(self.pet)
        self.display_manager.display_hunger(self.pet.hunger)
