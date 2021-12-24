import pygame


COLOUR_ACTIVE = (255, 255, 255)
COLOUR_INACTIVE = (0, 0, 0)
TEXT_COLOUR = (255, 255, 255)


class InputBox:
    """A class for user text input. Displays as a rectangle.

    Attributes:
            rect: Pygame rect object for the box.
            size: Size of the input box.
            colour: Colour of rectangle borders.
            text_colour: Colour of text inside box.
            text: Input text that is written in the box.
            text_surface: Pygame surface object for displaying the object.
    """

    def __init__(self, pos_x, pos_y, width, height):
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.size = (width, height)
        self.colour = COLOUR_INACTIVE
        self.text_colour = TEXT_COLOUR
        self.text = ""
        self.text_surface = pygame.font.Font(None, 32).render(
            self.text, True, self.text_colour
        )
        self.active = False

    def handle_event(self, event):
        """A function that handles all interactions a user can have with an InputBox.
        Updates box depending on interaction.

        Args:
            event: Pygame event (e.g. key press)
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
            self.colour = COLOUR_ACTIVE if self.active else COLOUR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.reset_surface()

    def draw(self, window):
        """Draws box surface on given surface.

        Args:
            window: a surface to be drawn on.
        """
        window.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 10))
        pygame.draw.rect(window, self.colour, self.rect, 1)

    def get_text(self):
        return self.text

    def reset(self):
        self.text = ""
        self.reset_surface()

    def reset_surface(self):
        self.text_surface = pygame.font.Font(None, 32).render(
            self.text, True, self.text_colour
        )
