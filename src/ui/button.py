import pygame


class Button:
    """A class that defines an user interface button.

    Attributes:
            position: A tuple of button X and Y coordinates in window.
            surface: A pygame Surface object which contains displayed button
            rect: A pygame Rect object which contains the button.
    """

    def __init__(self, text, pos_x, pos_y, text_colour, bg_colour):
        """A class constructor that creates a new button.

        Args:
            text: Text displayed on button.
            pos_x: X coordinate in window.
            pos_y: Y coordinate in window.
            text_colour: Displayed text colour in rgb.
            bg_colour: Displayed button background colour in rgb.
        """
        text_surface = pygame.font.Font(None, 32).render(text, True, text_colour)
        height = text_surface.get_height()
        width = text_surface.get_width()
        self.position = (pos_x, pos_y)
        self.surface = pygame.Surface((width, height))
        self.surface.fill(bg_colour)
        self.surface.blit(text_surface, (0, 0))
        self.rect = pygame.Rect(pos_x, pos_y, width, height)

    def get_rect(self):
        """Returns button rect to be interacted with.

        Returns: Button Rect object.
        """
        return self.rect

    def get_surface(self):
        """Returns button surface to be displayed

        Returns: Button surface.
        """
        return self.surface

    def draw(self, window):
        """Draws button surface (image) on given window.

        Args:
            window: Window to be drawn on.
        """
        window.blit(self.surface, self.position)
