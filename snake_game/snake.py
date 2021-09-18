import pygame

class Snake:

    def __init__(self, start_pos, radius, color, step):
        self.radius = radius
        self.body = [[start_pos[0]+(2*self.radius*(i)), start_pos[1]] for i in range(4)]
        self.color = color
        self.step = step
        self.vel = [-self.step, 0] # has two components x, y
        self.direction = "left"
        self.score = 0

    def move(self):
        new_circle = [self.body[0][0] + self.vel[0], self.body[0][1]+self.vel[1]]
        self.body = [new_circle] + self.body[:-1]

    def eat_fruit(self):
        self.body.append(self.body[-1])
        self.ate = False
        self.score += 1

    def draw(self, screen):
        for pos in self.body:
            pygame.draw.circle(screen, self.color, pos, self.radius)
