import pygame
from entities.game_sprite import GameSprite

LOGIN_REGISTER_BG_COLOUR = (84, 183, 166)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class DisplayManager:
    """A class that handles everything that is displayed.

    Attributes:
            window: The main window surface of the app.
            width: Main window width.
            height: Main window height.
            sprite_group: A pygame Group object containing current view sprites.
            image_loader: A helper object that loads all images.
            font: Main font of the app.
    """

    def __init__(self, window, image_loader):
        """A class constructor that creates a display manager.

        Args:
            window: The main window surface of the app.
            image_loader: A pygame Group object containing current view sprites.
        """
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.sprite_group = []
        self.image_loader = image_loader
        self.font = pygame.font.SysFont("Arial", 20)
        pygame.display.set_caption("Gacha pet")

    def flip(self):
        """A function that draws the window"""
        pygame.display.flip()

    def update_view_1(self, user, pet):
        """A function that creates main game view.

        Args:
            user: Contains all user data.
            pet: Contains all user pet data.
        """
        self.set_background()
        self.sprite_group.draw(self.window)
        self.display_money(user)
        self.display_hunger(pet)
        self.display_food(user)
        self.display_username(user.name)
        pygame.display.flip()

    def _view_2(self, user):
        self.window.fill((0, 0, 0))
        self.sprite_group.draw(self.window)
        self.display_money(user)
        self.display_food(user)

    def update_view_2(self, user):
        """A function that updates gacha view using only basic elements.

        Args:
            user: Contains all user data.
        """
        self._view_2(user)
        self.flip()

    def update_view_2_with_gacha(self, user, item):
        """A function that updates gacha view with gacha text.

        Args:
            user: Contains all user data.
            item: Name of the item got from gacha.
        """
        self._view_2(user)
        self.display_gacha(item)
        self.flip()

    def update_view_2_with_gacha_unsuccessful(self, user):
        """A function that updates gacha view when gacha game unsuccessful (no money).

        Args:
            user: Contains all user data.
        """
        self._view_2(user)
        self.display_no_money_message()
        self.flip()

    def _view_3(self, username_box, password_box, login_button, to_register_button):
        self.window.fill(LOGIN_REGISTER_BG_COLOUR)
        self._display_label("Username", 200, 180)
        username_box.draw(self.window)
        self._display_label("Password", 200, 280)
        password_box.draw(self.window)
        login_button.draw(self.window)
        to_register_button.draw(self.window)
        self.display_logo()

    def update_view_3(
        self, username_box, password_box, login_button, to_register_button
    ):
        """A function that updates login view using basic elements.

        Args:
            username_box: Username input box.
            password_box: Password input box.
            login_button: A button that is used to log in.
        """
        self._view_3(username_box, password_box, login_button, to_register_button)
        self.flip()

    def update_view_3_with_error(
        self, username_box, password_box, login_button, to_register_button
    ):
        """A function that updates login view when a login error has occurred.

        Args:
            username_box: Username input box.
            password_box: Password input box.
            login_button: A button that is used to log in.
        """
        self._view_3(username_box, password_box, login_button, to_register_button)
        self.display_login_error()
        self.flip()

    def _view_4(
        self,
        username_box,
        password_box,
        password_again_box,
        register_button,
        to_login_button,
    ):
        self.window.fill(LOGIN_REGISTER_BG_COLOUR)
        self._display_label("Username", 200, 180)
        username_box.draw(self.window)
        self._display_label("Password", 200, 280)
        password_box.draw(self.window)
        self._display_label("Password again", 190, 380)
        password_again_box.draw(self.window)
        register_button.draw(self.window)
        to_login_button.draw(self.window)
        self.display_logo()

    def update_view_4(
        self,
        username_box,
        password_box,
        password_again_box,
        register_button,
        back_button,
    ):
        self._view_4(
            username_box, password_box, password_again_box, register_button, back_button
        )
        self.flip()

    def update_view_4_with_error(
        self,
        username_box,
        password_box,
        password_again_box,
        register_button,
        back_button,
    ):
        self._view_4(
            username_box, password_box, password_again_box, register_button, back_button
        )
        self._display_view_4_error()
        self.flip()

    def _view_5(self, pet_name_box, continue_button):
        self.window.fill(LOGIN_REGISTER_BG_COLOUR)
        self._display_label("Pet name", 200, 180)
        pet_name_box.draw(self.window)
        continue_button.draw(self.window)
        self.display_logo()

    def update_view_5(self, pet_name_box, continue_button):
        self._view_5(pet_name_box, continue_button)
        self.flip()

    def update_view_5_with_error(self, pet_name_box, continue_button):
        self._view_5(pet_name_box, continue_button)
        self._display_view_5_error()
        self.flip()

    def create_view_1_sprites(self):
        """A function that creates main game view sprites and keeps a list of them.

        Returns:
                A list of all created sprite objects.
        """
        sprite_list = []
        loaded_images = self.image_loader.load_view_images(1)
        dog_sprite = GameSprite(225, 420, loaded_images[0])
        play_button_sprite = GameSprite(390, 40, loaded_images[1])
        coin_sprite = GameSprite(40, 805, loaded_images[2])
        food_sprite = GameSprite(160, 805, loaded_images[3])
        logout_sprite = GameSprite(400, 805, loaded_images[4])
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(dog_sprite)
        self.sprite_group.add(play_button_sprite)
        self.sprite_group.add(coin_sprite)
        self.sprite_group.add(food_sprite)
        self.sprite_group.add(logout_sprite)
        sprite_list.append(dog_sprite)
        sprite_list.append(play_button_sprite)
        sprite_list.append(coin_sprite)
        sprite_list.append(food_sprite)
        sprite_list.append(logout_sprite)
        return sprite_list

    def create_view_2_sprites(self):
        """A function that creates gacha view sprites and keeps a list of them.

        Returns:
                A list of all created sprite objects.
        """
        sprite_list = []
        loaded_images = self.image_loader.load_view_images(2)
        gacha_sprite = GameSprite(225, 420, loaded_images[0])
        arrow_sprite = GameSprite(40, 40, loaded_images[1])
        coin_sprite = GameSprite(40, 805, loaded_images[2])
        food_sprite = GameSprite(160, 805, loaded_images[3])
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(gacha_sprite)
        self.sprite_group.add(arrow_sprite)
        self.sprite_group.add(coin_sprite)
        self.sprite_group.add(food_sprite)
        sprite_list.append(gacha_sprite)
        sprite_list.append(arrow_sprite)
        sprite_list.append(coin_sprite)
        sprite_list.append(food_sprite)
        return sprite_list

    def display_money(self, user):
        """A function that creates text of user's money and displays it on main game window.

        Args:
            user: Contains all user data.
        """
        text = self.font.render(str(user.money), True, (255, 255, 255))
        self.window.blit(text, (65, 795))

    def display_hunger(self, pet):
        """A function that creates text of pet's hunger and displays it on main game window.

        Args:
            pet: Contains all pet data.
        """
        text = self.font.render(f"Hunger: {pet.hunger}", True, (255, 255, 255))
        self.window.blit(text, (250, 795))

    def display_gacha(self, item):
        """A function that creates text of the name of obtained item and displays it on
        main game window.

        Args:
            item: The name of obtained item.
        """
        text = self.font.render(f"You got {item}!", True, (255, 255, 255))
        self.window.blit(text, (150, 100))

    def display_food(self, user):
        """A function that creates text of number of food in user's posession and displays
        it on main game window.

        Args:
            user: Contains all user data.
        """
        text = self.font.render(str(user.food), True, (255, 255, 255))
        self.window.blit(text, (195, 795))

    def display_no_money_message(self):
        """A function that creates text that informs user that they do not have enough money
        to play gacha and displays it on main game window.

        Args:
            user: Contains all user data.
        """
        text = self.font.render("Not enough money", True, (255, 255, 255))
        self.window.blit(text, (150, 100))

    def display_username(self, username):
        """A function that creates text of the username and displays it on main game window.

        Args:
            username: The name of the user.
        """
        text = self.font.render(username, True, (0, 0, 0))
        self.window.blit(text, (20, 20))

    def set_background(self):
        """A function that loads and sets the background to the main screen."""
        image = self.image_loader.load_background()
        self.window.blit(image, (0, 0))

    def display_logo(self):
        """A function that loads and displays game logo in login screen."""
        logo = self.image_loader.load_logo()
        self.window.blit(logo, (25, 50))

    def display_login_error(self):
        """A function that creates and displays login error text."""
        text = self.font.render("Incorrect username or password", True, BLACK)
        self.window.blit(text, (100, 360))

    def _display_label(self, text, pos_x, pos_y):
        font = pygame.font.SysFont("Arial", 12)
        text_surface = font.render(text, True, BLACK)
        self.window.blit(text_surface, (pos_x, pos_y))

    def _display_view_4_error(self):
        font = pygame.font.SysFont("Arial", 12)
        text = font.render(
            "Error in registrarion. Check passwords or change username", True, BLACK
        )
        self.window.blit(text, (80, 480))

    def _display_view_5_error(self):
        text = self.font.render("Incorrect pet name", True, BLACK)
        self.window.blit(text, (160, 250))
