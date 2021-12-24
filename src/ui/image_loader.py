import pygame

VIEW_1_IMAGES = [
    "src/media/dog1.png",
    "src/media/playbutton.png",
    "src/media/coin.png",
    "src/media/food.png",
    "src/media/logout_white.png",
]
VIEW_2_IMAGES = [
    "src/media/gacha1.png",
    "src/media/arrow.png",
    "src/media/coin.png",
    "src/media/food.png",
]


class ImageLoader:
    """A class for looading pygame images."""

    def load_view_images(self, view):
        """A function for loading view images.

        Args:
            view: View number.

        Returns: A list of loaded images."""
        loaded_images = []
        if view == 1:
            for url in VIEW_1_IMAGES:
                loaded_images.append(pygame.image.load(url))
        elif view == 2:
            for url in VIEW_2_IMAGES:
                loaded_images.append(pygame.image.load(url))
        return loaded_images

    def load_background(self):
        """A function for loading main game background image.

        Returns: Loaded background image.
        """
        return pygame.image.load("src/media/garden.png")

    def load_logo(self):
        """A function for loading application logo.

        Returns: Loaded logo image.
        """
        return pygame.image.load("src/media/logo.png")
