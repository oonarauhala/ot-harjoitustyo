import pygame

VIEW_1_IMAGES = ["src/media/dog1.png", "src/media/playbutton.png", "src/media/coin.png"]
VIEW_2_IMAGES = ["src/media/gacha1.png", "src/media/arrow.png", "src/media/coin.png"]


class ImageLoader:
    def load_view_images(self, view):
        loaded_images = []
        if view == 1:
            for url in VIEW_1_IMAGES:
                loaded_images.append(pygame.image.load(url))
        elif view == 2:
            for url in VIEW_2_IMAGES:
                loaded_images.append(pygame.image.load(url))
        return loaded_images

    def load_background(self):
        return pygame.image.load("src/media/garden.png")
