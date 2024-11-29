import pygame
from settings import *
from sprites import *
import random

class Game:
    pattern_step = 0
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.flashcolors = [yellow, blue ,red, green]
        self.colors = [darkyellow, darkblue, darkred, darkgreen]
        self.buttons = [
            button(110, 50 , darkyellow),
            button(330, 50 , darkblue),
            button(110, 270 , darkred),
            button(330, 270 , darkgreen),
        ]
    def new(self):
        self.waiting_input = False
        self.pattern = []
        self.current_step = 0
        self.score = 0
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(fps)
            self.clicked_button = None
            self.event()
            self.draw()
            self.update()
    def update(self):
        if not self.waiting_input:
            pygame.time.wait(1000)
            self.pattern.append(random.choice(self.colors))
            for button in self.pattern:
                self.button_animation(button)
                pygame.time.wait(200)
            self.waiting_input = True
        else:
            # correct button
            if self.clicked_button and self.clicked_button == self.pattern[self.current_step]:
                self.button_animation(self.clicked_button)
                self.current_step += 1
            # last button
            if self.current_step == len(self.pattern):
                self.score += 1
                self.waiting_input = False
                self. current_step = 0
                self.pattern_step += 1
            # wrong button
            elif self.clicked_button and self.clicked_button == self.pattern[self.current_step]:
                self.game_over_animation()
                self.playing = False
    def button_animation(self, color):
        for i in range(len(self.colors)):
            if self.colors[i] == color:
                flash_color = self.flashcolors[i]
        original_surface = self.screen.copy()
        flash_surface = pygame.Surface((buttonsize, buttonsize))
        flash_surface = flash_surface.convert_alpha()
        r, g, b = flash_color
        for start, end, step in ((0, 255, 1), (255, 0, -1)):
            for alpha in range(start, end, animationspeed * step):
                self.screen.blit(original_surface, (0, 0))
                flash_surface.fill((r, g, b, alpha))
                self.screen.blit(flash_surface, (0, 0))
                pygame.display.update()
                self.clock.tick(fps)
        self.screen.blit(original_surface, (0, 0))
    def game_over_animation(self):
        original_surface = self.screen.copy()
        flash_surface = pygame.Surface((buttonsize, buttonsize))
        flash_surface = flash_surface.convert_alpha()
        r, g, b = white
        for _ in range (3):
            for start, end, step in ((0, 255, 1), (255, 0, -1)):
                for alpha in range(start, end, animationspeed * step):
                    self.screen.blit(original_surface, (button.x, button.y))
                    flash_surface.fill((r, g, b, alpha))
                    self.screen.blit(flash_surface, (0, 0))
                    pygame.display.update()
                    self.clock.tick(fps)
    def draw(self):
        self.screen.fill(bgcolor)
        UIElement(170, 20, f"score: {str(self.score)}").draw(self.screen)
        for button in self.buttons:
            button.draw(self.screen)
        pygame.display.update()
    def event(self):
        for event in pygame.event.get():
            if event.type == quit:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.clicked(mouse_x, mouse_y):
                        self.clicked_button = button.color

game = Game()
while game.pattern_step < 6:
    game.new()
    game.run()
    if game.playing == False:
        pygame.quit