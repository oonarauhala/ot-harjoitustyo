import sys
import pygame
from entities.display_manager import DisplayManager
from entities.item_machine import ItemMachine
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
        self.item_machine = ItemMachine()
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
                        # Click pet sprite
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
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = event.pos
                        # Click gacha
                        if self.sprites[0].rect.collidepoint(position):
                            self.play_gacha()
                        # Click arrow
                        if self.sprites[1].rect.collidepoint(position):
                            self.change_view(1)

    def feed_pet(self):
        self.user.feed_pet(self.pet)
        self.display_manager.update_view_1(self.user, self.pet)

    def play_gacha(self):
        item = self.item_machine.generate_item()
        self.user.recieve_item(item)
        self.display_manager.update_view_2_with_gacha(self.user, item)

    def change_view(self, view):
        self.kill_all_sprites()
        if view == 1:
            self.sprites = self.display_manager.create_view_1_sprites()
            self.display_manager.update_view_1(self.user, self.pet)
            self.view = 1
        if view == 2:
            self.sprites = self.display_manager.create_view_2_sprites()
            self.display_manager.update_view_2(self.user)
            self.view = 2

    def kill_all_sprites(self):
        self.sprites = []
