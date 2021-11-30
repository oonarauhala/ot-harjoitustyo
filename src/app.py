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
        self.sprites = []
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
                        if self.sprites[0].rect.collidepoint(position):
                            if self.pet.is_hungry():
                                self.feed_pet()
                        # Click gacha button
                        if self.sprites[1].rect.collidepoint(position):
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
            self.sprites = self.display_manager.create_view_1_sprites()
            self.display_manager.display_hunger(self.pet.hunger)
            self.view = 1
        if view == 2:
            self.sprites = self.display_manager.create_view_2_sprites()
            self.display_manager.change_to_gacha_view_()
            self.view = 2

    def kill_all_sprites(self):
        self.sprites = []
