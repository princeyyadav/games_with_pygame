import pygame

class Text:

    def __init__(self, text, fontstyle="Arial", size=32, bold=True, pos=(10,10), color=(255, 255, 255)):
        self.text = text
        self.pos = pos
        self.color = color
        self.font = pygame.font.SysFont(fontstyle, size, bold)

    def update(self, text):
        self.text = text

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, self.pos)