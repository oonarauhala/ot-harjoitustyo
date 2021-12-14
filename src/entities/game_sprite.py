import pygame


class GameSprite(pygame.sprite.Sprite):
    """A custom pygame Sprite class that creates sprites with images.

    Attributes:
        image: Image to be displayed.
        rect: A pygame Rect object containing the sprite.
    """

    def __init__(self, pos_x, pos_y, image):
        """A class constructor for creating GameSprite objects.

        Args:
            pos_x: X coordinate in game window.
            pos_y: Y coordinate in game window.
            image: Image to be displayed on sprite.
        """
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
