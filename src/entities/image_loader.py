import pygame

UI_IMAGES = ["src/media/gacha1.png", "src/media/playbutton.png"]
DOG_SPRITE_IMAGES = ["src/media/dog1.png"]


class ImageLoader:
    def load_dog_images(self):
        loaded_sprite_images = []
        for url in DOG_SPRITE_IMAGES:
            loaded_sprite_images.append(pygame.image.load(url))
        return loaded_sprite_images

    def load_ui_images(self):
        loaded_ui_images = []
        for url in UI_IMAGES:
            loaded_ui_images.append(pygame.image.load(url))
        return loaded_ui_images
