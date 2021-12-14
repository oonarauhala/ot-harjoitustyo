import sys
import pygame
from entities.display_manager import DisplayManager
from entities.item_machine import ItemMachine
from entities.pet import Pet
from entities.user import User
from entities.image_loader import ImageLoader
from entities.hunger_generator import HungerGenerator
from entities.input_box import InputBox
from entities.button import Button
from entities.user_repository import UserRepository

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class App:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(200, 25)
        resolution = (450, 840)
        self.username_input_box = InputBox(130, 200, 200, 40)
        self.password_input_box = InputBox(130, 300, 200, 40)
        self.login_button = Button("Login", 0, 0, BLACK, WHITE)
        self.display_manager = DisplayManager(
            pygame.display.set_mode(resolution), ImageLoader()
        )
        self.item_machine = ItemMachine()
        self.clock = pygame.time.Clock()
        self.hunger_generator = HungerGenerator()
        self.sprites = []
        self.pet = Pet("Pottu", "dog")
        self.user = User()
        self.user_repository = UserRepository()
        self.view = 0

    def run(self):
        self.change_view(3)
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
            if self.view == 3:
                self.display_manager.update_view_3(
                    self.username_input_box, self.password_input_box, self.login_button
                )
                for event in pygame.event.get():
                    self.username_input_box.handle_event(event)
                    self.password_input_box.handle_event(event)
                    # self.login_button.click(event)
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = event.pos
                        if self.login_button.get_rect().collidepoint(position):
                            username = self.username_input_box.get_text()
                            password = self.password_input_box.get_text()
                            self.user.nimi = username
                            if self.user_repository.login(username, password):
                                self.change_view(1)

            if self.hunger_generator.generate_hunger() and self.view == 1:
                self.pet.get_hungrier()
                self.display_manager.update_view_1(self.user, self.pet)
            self.clock.tick(30)

    def feed_pet(self):
        self.user.feed_pet(self.pet)
        self.display_manager.update_view_1(self.user, self.pet)

    def play_gacha(self):
        if self.user.pay():
            item = self.item_machine.generate_item()
            self.user.recieve_item(item)
            self.display_manager.update_view_2_with_gacha(self.user, item)
        else:
            self.display_manager.update_view_2_with_gacha_unsuccessful(self.user)

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
        if view == 3:
            self.display_manager.update_view_3(
                self.username_input_box, self.password_input_box, self.login_button
            )
            self.view = 3

    def kill_all_sprites(self):
        self.sprites = []
