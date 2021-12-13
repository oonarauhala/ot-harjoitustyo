import pygame


class Button:
    def __init__(self, text, pos_x, pos_y, text_colour, bg_colour):
        text_surface = pygame.font.Font(None, 32).render(text, True, text_colour)
        height = text_surface.get_height()
        width = text_surface.get_width()
        self.surface = pygame.Surface((width, height))
        self.surface.fill(bg_colour)
        self.surface.blit(text_surface, (0, 0))
        self.rect = pygame.Rect(pos_x, pos_y, width, height)

    def get_rect(self):
        return self.rect

    def get_surface(self):
        return self.surface

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                pass
