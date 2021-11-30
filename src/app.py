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
        self.ui_sprites = []
        self.pet_sprites = []
        self.pet = Pet("Pottu", "dog")
        self.user = User()
        self.view = 1

    def run(self):
        self.change_view(1)
        while True:
            if self.view == 1:
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
                            self.change_view(2)
            if self.view == 2:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

    def feed_pet(self):
        self.user.feed_pet(self.pet)
        self.display_manager.display_hunger(self.pet.hunger)

    def change_view(self, view):
        self.kill_all_sprites()
        if view == 1:
            self.ui_sprites = self.display_manager.create_view_1_ui_sprites()
            self.pet_sprites = self.display_manager.create_pet_sprites()
            self.display_manager.display_hunger(self.pet.hunger)
        if view == 2:
            self.display_manager.change_to_gacha_view_()
            self.view = 2

    def kill_all_sprites(self):
        self.pet_sprites = []
        self.ui_sprites = []
