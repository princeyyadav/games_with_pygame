import pygame, random

class Fruit:

    colors = (
        (215, 0, 0), # red
        (215, 96, 0), # orange
        (228, 222, 67), # yellow
        (179, 84, 136), #  purple
    )

    def __init__(self, radius, step):
        self.radius = radius
        self.step = step
        self.pos = [400,200]
        self.color = random.choice(Fruit.colors)

    def respawn(self, w, h):
        self.color = random.choice(Fruit.colors)
        self.pos[0] = ( random.randint(2*self.radius, w - (2*self.radius))//self.step )*self.step
        self.pos[1] = ( random.randint(2*self.radius, h - (2*self.radius))//self.step )*self.step

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
