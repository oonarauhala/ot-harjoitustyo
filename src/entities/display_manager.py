import pygame
from entities.game_sprite import GameSprite


class DisplayManager:
    def __init__(self, window, image_loader):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.pet_sprite_group = []
        self.ui_sprite_group = []
        self.image_loader = image_loader
        self.font = pygame.font.SysFont("Arial", 20)
        pygame.display.set_caption("Gacha pet")

    def update(self):
        self.window.fill((0, 0, 0))
        self.pet_sprite_group.draw(self.window)
        self.ui_sprite_group.draw(self.window)
        pygame.display.flip()

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

    def display_hunger(self, amount):
        self.update()
        text = self.font.render(f"Hunger: {amount}", True, (255, 255, 255))
        self.window.blit(text, (50, 50))
        pygame.display.flip()

    def change_view_(self, sprites):
        pass
