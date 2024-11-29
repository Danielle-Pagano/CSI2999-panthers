import pygame
from settings import *
class button:
    def __init__(self, x, y, color):
        self.x, self.y = x, y
        self.color = color
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, buttonsize, buttonsize))
    def clicked(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + buttonsize and self.y <= mouse_y <= self.y + buttonsize
class UIElement:
    def __init__(self, x, y, text):
        self.x, self.y = x, y
        self.text = text
    def draw(self, screen):
        font = pygame.font.SysFont("Arial", 16)
        text = font.render(self.text , True, white)
        screen.blit(text, (self.x, self.y))