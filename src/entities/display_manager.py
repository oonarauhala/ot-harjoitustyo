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

    def update_view_1(self, user, pet):
        self.set_background()
        self.sprite_group.draw(self.window)
        self.display_money(user)
        self.display_hunger(pet)
        self.display_food(user)
        pygame.display.flip()

    def update_view_2(self, user):
        self.window.fill((0, 0, 0))
        self.sprite_group.draw(self.window)
        self.display_money(user)
        self.display_food(user)
        pygame.display.flip()

    def update_view_3(self, username_box, password_box):
        self.window.fill((0, 0, 0))
        username_box.draw(self.window)
        password_box.draw(self.window)
        pygame.display.flip()

    def update_view_2_with_gacha(self, user, item):
        self.window.fill((0, 0, 0))
        self.sprite_group.draw(self.window)
        self.display_money(user)
        self.display_gacha(item)
        self.display_food(user)
        pygame.display.flip()

    def update_view_2_with_gacha_unsuccessful(self, user):
        self.window.fill((0, 0, 0))
        self.sprite_group.draw(self.window)
        self.display_money(user)
        self.display_food(user)
        self.display_no_money_message()
        pygame.display.flip()

    def create_view_1_sprites(self):
        sprite_list = []
        loaded_images = self.image_loader.load_view_images(1)
        dog_sprite = GameSprite(225, 420, loaded_images[0])
        play_button_sprite = GameSprite(390, 40, loaded_images[1])
        coin_sprite = GameSprite(40, 805, loaded_images[2])
        food_sprite = GameSprite(180, 805, loaded_images[3])
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(dog_sprite)
        self.sprite_group.add(play_button_sprite)
        self.sprite_group.add(coin_sprite)
        self.sprite_group.add(food_sprite)
        sprite_list.append(dog_sprite)
        sprite_list.append(play_button_sprite)
        sprite_list.append(coin_sprite)
        sprite_list.append(food_sprite)
        return sprite_list

    def create_view_2_sprites(self):
        sprite_list = []
        loaded_images = self.image_loader.load_view_images(2)
        gacha_sprite = GameSprite(225, 420, loaded_images[0])
        arrow_sprite = GameSprite(40, 40, loaded_images[1])
        coin_sprite = GameSprite(40, 805, loaded_images[2])
        food_sprite = GameSprite(180, 805, loaded_images[3])
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
        text = self.font.render(str(user.money), True, (255, 255, 255))
        self.window.blit(text, (65, 795))

    def display_hunger(self, pet):
        text = self.font.render(f"Hunger: {pet.hunger}", True, (255, 255, 255))
        self.window.blit(text, (300, 795))

    def display_gacha(self, item):
        text = self.font.render(f"You got {item}!", True, (255, 255, 255))
        self.window.blit(text, (150, 100))

    def display_food(self, user):
        text = self.font.render(str(user.food), True, (255, 255, 255))
        self.window.blit(text, (215, 795))

    def display_no_money_message(self):
        text = self.font.render("Not enough money", True, (255, 255, 255))
        self.window.blit(text, (150, 100))

    def set_background(self):
        image = self.image_loader.load_background()
        self.window.blit(image, (0, 0))
