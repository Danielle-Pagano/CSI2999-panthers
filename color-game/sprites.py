import pygame
from settings import *

font_name = pygame.font.match_font('Arial')

class button:
    def __init__(self, x, y, color):
        self.x, self.y = x, y
        self.color = color
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, buttonsize, buttonsize))
    def clicked(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + buttonsize and self.y <= mouse_y <= self.y + buttonsize

class QuitButton:
        def __init__(self, x, y, color, text):
            self.x, self.y = x, y
            self.color = color
            self.text = text
        def draw(self, screen):
            pygame.draw.rect(screen, self.color, (self.x, self.y, buttonwidth, buttonheight))
            font = pygame.font.Font(font_name, 20)
            text_surface = font.render(self.text, True, black)
            text_rect = text_surface.get_rect(center=(self.x + buttonwidth // 2, self.y + buttonheight // 2))
            screen.blit(text_surface, text_rect)

        def clicked(self, mouse_x, mouse_y):
            if self.x <= mouse_x <= self.x + buttonwidth and self.y <= mouse_y <= self.y + buttonheight:
                pygame.quit()


class UIElement:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text
    def draw(self, screen):
        font = pygame.font.SysFont("Arial", 16)
        text = font.render(self.text , True, white)
        screen.blit(text, (self.x, self.y))