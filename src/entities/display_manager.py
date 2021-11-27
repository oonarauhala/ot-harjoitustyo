import pygame
from entities.game_sprite import GameSprite


class DisplayManager:
    def __init__(self, window, image_loader):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.image_loader = image_loader

    def init_window(self, resolution):
        pygame.display.set_caption("Gacha pet")
        self.window.fill((0, 0, 0))
        pygame.display.flip()

    def update(self):
        pygame.display.flip()
        self.pet_sprite_group.draw(self.window)
        self.ui_sprite_group.draw(self.window)

    def create_ui_sprites(self):
        ui_sprite_list = []
        loaded_ui_images = self.image_loader.load_ui_images()
        play_button_sprite = GameSprite(390, 40, loaded_ui_images[1])
        self.ui_sprite_group = pygame.sprite.Group()
        self.ui_sprite_group.add(play_button_sprite)
        ui_sprite_list.append(play_button_sprite)
        return ui_sprite_list

    def create_pet_sprites(self):
        pet_sprite_list = []
        loaded_pet_images = self.image_loader.load_dog_images()
        dog_sprite = GameSprite(225, 420, loaded_pet_images[0])
        self.pet_sprite_group = pygame.sprite.Group()
        self.pet_sprite_group.add(dog_sprite)
        pet_sprite_list.append(dog_sprite)
        return pet_sprite_list

    def change_view_(self, sprites):
        pass
