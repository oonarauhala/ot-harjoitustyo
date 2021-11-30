import pygame
from entities.game_sprite import GameSprite


class DisplayManager:
    def __init__(self, window, image_loader):
        self.window = window
        self.width = window.get_width()
        self.height = window.get_height()
        self.sprite_group = []
        self.image_loader = image_loader
        self.font = pygame.font.SysFont("Arial", 20)
        pygame.display.set_caption("Gacha pet")

    def update(self):
        self.window.fill((0, 0, 0))
        self.sprite_group.draw(self.window)
        pygame.display.flip()

    def create_view_1_sprites(self):
        sprite_list = []
        loaded_images = self.image_loader.load_view_images(1)
        dog_sprite = GameSprite(225, 420, loaded_images[0])
        play_button_sprite = GameSprite(390, 40, loaded_images[1])
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(dog_sprite)
        self.sprite_group.add(play_button_sprite)
        sprite_list.append(dog_sprite)
        sprite_list.append(play_button_sprite)
        return sprite_list

    def create_view_2_sprites(self):
        sprite_list = []
        loaded_images = self.image_loader.load_view_images(2)
        gacha_sprite = GameSprite(225, 420, loaded_images[0])
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(gacha_sprite)
        sprite_list.append(gacha_sprite)
        return sprite_list

    def display_hunger(self, amount):
        self.update()
        text = self.font.render(f"Hunger: {amount}", True, (255, 255, 255))
        self.window.blit(text, (50, 50))
        pygame.display.flip()

    def change_to_gacha_view_(self):
        sprites = self.create_view_2_sprites()
        self.update()
        return sprites
