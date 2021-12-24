import sys
import pygame


class App:
    """A class for main application loop. Detects all user interaction and
    delegates them to right objects.

    Attributes:
            user_repository: An object that holds all user data.
            display_manager: An object that handles ui display.
            item_machine: Generates random items.
            hunger_generator: Generates pet hunger randomly.
            *_box: box For user inputs.
            *_button: Button for user ineraction.
            clock: Game clock.
            sprites: A list of game sprites.
            view: Number of current view.
            *_error: Holds information about current view error occurance.
    """

    def __init__(
        self,
        user_repository,
        display_manager,
        item_machine,
        hunger_generator,
        input_boxes,
        login_button,
        register_button,
        to_login_button,
        to_register_button,
        continue_button,
    ):
        self.login_username_input_box = input_boxes[0]
        self.login_password_input_box = input_boxes[1]
        self.register_username_input_box = input_boxes[2]
        self.register_password_input_box = input_boxes[3]
        self.register_password_again_input_box = input_boxes[4]
        self.pet_name_box = input_boxes[5]
        self.login_button = login_button
        self.register_button = register_button
        self.to_login_button = to_login_button
        self.to_register_button = to_register_button
        self.continue_button = continue_button
        self.display_manager = display_manager
        self.item_machine = item_machine
        self.clock = pygame.time.Clock()
        self.hunger_generator = hunger_generator
        self.sprites = []
        self.user_repository = user_repository
        self.view = 0
        self.login_error = False
        self.register_error = False
        self.pet_name_error = False

    def run(self):
        """Main loop function. Checks current vien and acts accordingly.
        Initiates hunger generation.
        """
        self._change_view(3)
        while True:
            if self.view == 1:
                self._handle_view_1()
            elif self.view == 2:
                self._handle_view_2()
            elif self.view == 3:
                self._handle_view_3()
            elif self.view == 4:
                self._handle_view_4()
            elif self.view == 5:
                self._handle_view_5()

            if self.hunger_generator.generate_hunger() and self.view == 1:
                self.user_repository.user.pet.get_hungrier()
                self.display_manager.update_view_1(
                    self.user_repository.user, self.user_repository.user.pet
                )
            self.clock.tick(30)

    def _handle_view_1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                # Click pet sprite
                if self.sprites[0].rect.collidepoint(position):
                    if self.user_repository.user.pet.is_hungry():
                        self._feed_pet()
                # Click gacha button
                if self.sprites[1].rect.collidepoint(position):
                    self._change_view(2)
                try:
                    if self.sprites[4].rect.collidepoint(position):
                        self._logout()
                except RuntimeError:
                    pass

    def _handle_view_2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = event.pos
                # Click gacha
                if self.sprites[0].rect.collidepoint(position):
                    self._play_gacha()
                # Click arrow
                if self.sprites[1].rect.collidepoint(position):
                    self._change_view(1)

    def _handle_view_3(self):
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
                # Click login button
                if self.login_button.get_rect().collidepoint(position):
                    username = self.login_username_input_box.get_text()
                    password = self.login_password_input_box.get_text()
                    if self.user_repository.login(username, password):
                        self._change_view(1)
                    else:
                        self.login_error = True
                        self.display_manager.update_view_3_with_error(
                            self.login_username_input_box,
                            self.login_password_input_box,
                            self.login_button,
                            self.to_register_button,
                        )
                # Click register button
                elif self.to_register_button.get_rect().collidepoint(position):
                    self._change_view(4)

    def _handle_view_4(self):
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
                    password_again = self.register_password_again_input_box.get_text()
                    if password == password_again:
                        if self.user_repository.register(username, password):
                            self._change_view(5)
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
                    self._change_view(3)

    def _handle_view_5(self):
        if not self.pet_name_error:
            self.display_manager.update_view_5(self.pet_name_box, self.continue_button)
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
                        self._change_view(1)
                    else:
                        self.pet_name_error = True
                        self.display_manager.update_view_5_with_error(
                            self.pet_name_box, self.continue_button
                        )

    def _feed_pet(self):
        self.user_repository.user.feed_pet(self.user_repository.user.pet)
        self.display_manager.update_view_1(
            self.user_repository.user, self.user_repository.user.pet
        )

    def _play_gacha(self):
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

    def _logout(self):
        self.user_repository.logout()
        self._reset_input_boxes()
        self._change_view(3)

    def _change_view(self, view):
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
