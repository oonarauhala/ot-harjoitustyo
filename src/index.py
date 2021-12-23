import pygame

from app import App
from entities.hunger_generator import HungerGenerator
from entities.item_machine import ItemMachine
from entities.pet import Pet
from entities.user import User
from entities.validator import Validator
from repositories.user_repository import UserRepository
from ui.button import Button
from ui.display_manager import DisplayManager
from ui.image_loader import ImageLoader
from ui.input_box import InputBox

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    pygame.init()
    pygame.key.set_repeat(200, 25)
    pet = Pet()
    user = User(pet)
    validator = Validator()
    user_repository = UserRepository(validator, user)
    resolution = (450, 840)
    display_manager = DisplayManager(pygame.display.set_mode(resolution), ImageLoader())
    item_machine = ItemMachine()
    hunger_generator = HungerGenerator()
    input_boxes = [
        InputBox(130, 200, 200, 40),
        InputBox(130, 300, 200, 40),
        InputBox(130, 200, 200, 40),
        InputBox(130, 300, 200, 40),
        InputBox(130, 400, 200, 40),
        InputBox(130, 200, 200, 40),
    ]
    login_button = Button("Login", 200, 400, BLACK, WHITE)
    register_button = Button("Register", 200, 500, BLACK, WHITE)
    to_login_button = Button("Login", 200, 600, BLACK, WHITE)
    to_register_button = Button("Register", 200, 500, BLACK, WHITE)
    continue_button = Button("Continue", 200, 300, BLACK, WHITE)
    app = App(
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
    )
    app.run()


if __name__ == "__main__":
    main()
