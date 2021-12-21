import sys
import pygame
from entities.display_manager import DisplayManager
from entities.item_machine import ItemMachine
from entities.pet import Pet
from entities.image_loader import ImageLoader
from entities.hunger_generator import HungerGenerator
from entities.input_box import InputBox
from entities.button import Button

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class App:
    def __init__(self, user_repository):
        pygame.init()
        pygame.key.set_repeat(200, 25)
        resolution = (450, 840)
        self.login_username_input_box = InputBox(130, 200, 200, 40)
        self.login_password_input_box = InputBox(130, 300, 200, 40)
        self.register_username_input_box = InputBox(130, 200, 200, 40)
        self.register_password_input_box = InputBox(130, 300, 200, 40)
        self.register_password_again_input_box = InputBox(130, 400, 200, 40)
        self.pet_name_box = InputBox(130, 200, 200, 40)
        self.login_button = Button("Login", 200, 400, BLACK, WHITE)
        self.register_button = Button("Register", 200, 500, BLACK, WHITE)
        self.to_login_button = Button("Login", 200, 600, BLACK, WHITE)
        self.to_register_button = Button("Register", 200, 500, BLACK, WHITE)
        self.continue_button = Button("Continue", 200, 300, BLACK, WHITE)
        self.display_manager = DisplayManager(
            pygame.display.set_mode(resolution), ImageLoader()
        )
        self.item_machine = ItemMachine()
        self.clock = pygame.time.Clock()
        self.hunger_generator = HungerGenerator()
        self.sprites = []
        self.user_repository = user_repository
        self.view = 0
        self.login_error = False
        self.register_error = False
        self.pet_name_error = False

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
                            if self.user_repository.user.pet.is_hungry():
                                self.feed_pet()
                        # Click gacha button
                        if self.sprites[1].rect.collidepoint(position):
                            self.change_view(2)
                        try:
                            if self.sprites[4].rect.collidepoint(position):
                                self.logout()
                        except:
                            pass
            elif self.view == 2:
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
            elif self.view == 3:
                self.handle_view_3()
            elif self.view == 4:
                if not self.register_error:
                    self.display_manager.update_view_4(
                        self.register_username_input_box,
                        self.register_password_input_box,
                        self.register_password_again_input_box,
                        self.register_button,
                        self.to_login_button,
                    )
                else:
                    self.display_manager.update_view_4_with_error(
                        self.register_username_input_box,
                        self.register_password_input_box,
                        self.register_password_again_input_box,
                        self.register_button,
                        self.to_login_button,
                    )
                for event in pygame.event.get():
                    self.register_username_input_box.handle_event(event)
                    self.register_password_input_box.handle_event(event)
                    self.register_password_again_input_box.handle_event(event)
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = event.pos
                        if self.register_button.get_rect().collidepoint(position):
                            username = self.register_username_input_box.get_text()
                            password = self.register_password_input_box.get_text()
                            password_again = (
                                self.register_password_again_input_box.get_text()
                            )
                            if password == password_again:
                                if self.user_repository.register(username, password):
                                    self.change_view(5)
                                else:
                                    self.register_error = True
                                    self.display_manager.update_view_4_with_error(
                                        self.register_username_input_box,
                                        self.register_password_input_box,
                                        self.register_password_again_input_box,
                                        self.register_button,
                                        self.to_login_button,
                                    )
                            else:
                                self.register_error = True
                                self.display_manager.update_view_4_with_error(
                                    self.register_username_input_box,
                                    self.register_password_input_box,
                                    self.register_password_again_input_box,
                                    self.register_button,
                                    self.to_login_button,
                                )
                        if self.to_login_button.get_rect().collidepoint(position):
                            self.change_view(3)
            elif self.view == 5:
                if not self.pet_name_error:
                    self.display_manager.update_view_5(
                        self.pet_name_box, self.continue_button
                    )
                else:
                    self.display_manager.update_view_5_with_error(
                        self.pet_name_box, self.continue_button
                    )
                for event in pygame.event.get():
                    self.pet_name_box.handle_event(event)
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = event.pos
                        if self.continue_button.get_rect().collidepoint(position):
                            pet_name = self.pet_name_box.get_text()
                            if len(pet_name) > 1:
                                self.user_repository.complete_registration(pet_name)
                                self.change_view(1)
                            else:
                                self.pet_name_error = True
                                self.display_manager.update_view_5_with_error(
                                    self.pet_name_box, self.continue_button
                                )

            if self.hunger_generator.generate_hunger() and self.view == 1:
                self.user_repository.user.pet.get_hungrier()
                self.display_manager.update_view_1(
                    self.user_repository.user, self.user_repository.user.pet
                )
            self.clock.tick(30)

    def handle_view_3(self):
        if not self.login_error:
            self.display_manager.update_view_3(
                self.login_username_input_box,
                self.login_password_input_box,
                self.login_button,
                self.to_register_button,
            )
        else:
            self.display_manager.update_view_3_with_error(
                self.login_username_input_box,
                self.login_password_input_box,
                self.login_button,
                self.to_register_button,
            )

        for event in pygame.event.get():
            self.login_username_input_box.handle_event(event)
            self.login_password_input_box.handle_event(event)
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                if self.login_button.get_rect().collidepoint(position):
                    username = self.login_username_input_box.get_text()
                    password = self.login_password_input_box.get_text()
                    if self.user_repository.login(username, password):
                        self.change_view(1)
                    else:
                        self.login_error = True
                        self.display_manager.update_view_3_with_error(
                            self.login_username_input_box,
                            self.login_password_input_box,
                            self.login_button,
                            self.to_register_button,
                        )
                elif self.to_register_button.get_rect().collidepoint(position):
                    self.change_view(4)

    def feed_pet(self):
        self.user_repository.user.feed_pet(self.user_repository.user.pet)
        self.display_manager.update_view_1(
            self.user_repository.user, self.user_repository.user.pet
        )

    def play_gacha(self):
        if self.user_repository.user.pay():
            item = self.item_machine.generate_item()
            self.user_repository.user.recieve_item(item)
            self.display_manager.update_view_2_with_gacha(
                self.user_repository.user, item
            )
        else:
            self.display_manager.update_view_2_with_gacha_unsuccessful(
                self.user_repository.user
            )

    def logout(self):
        self.user_repository.logout()
        self._reset_input_boxes()
        self.change_view(3)

    def change_view(self, view):
        self._reset_input_boxes()
        self._kill_all_sprites()
        if view == 1:
            self.sprites = self.display_manager.create_view_1_sprites()
            self.display_manager.update_view_1(
                self.user_repository.user, self.user_repository.user.pet
            )
            self.view = 1
        if view == 2:
            self.sprites = self.display_manager.create_view_2_sprites()
            self.display_manager.update_view_2(self.user_repository.user)
            self.view = 2
        if view == 3:
            self.display_manager.update_view_3(
                self.login_username_input_box,
                self.login_password_input_box,
                self.login_button,
                self.to_register_button,
            )
            self.view = 3
        if view == 4:
            self.display_manager.update_view_4(
                self.register_username_input_box,
                self.register_password_input_box,
                self.register_password_again_input_box,
                self.register_button,
                self.to_login_button,
            )
            self.view = 4
        if view == 5:
            self.display_manager.update_view_5(self.pet_name_box, self.continue_button)
            self.view = 5

    def _kill_all_sprites(self):
        self.sprites = []

    def _reset_input_boxes(self):
        self.login_username_input_box.reset()
        self.login_password_input_box.reset()
        self.register_password_again_input_box.reset()
        self.register_password_input_box.reset()
        self.register_username_input_box.reset()
        self.login_error = False
        self.register_error = False
