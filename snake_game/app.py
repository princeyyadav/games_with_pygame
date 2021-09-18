import pygame
from snake import Snake
from fruit import Fruit
from text import Text

pygame.init()

w, h = 500, 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("SNAKE GAME")
bg_color = (134, 220, 110) # light green

step = 20
snake = Snake([300,300], 10, (218, 60, 99), step)
print(snake.body)
apple = Fruit(11, step)
score_text = Text("Score: 0")

fps = 60
clock = pygame.time.Clock()

timer = 0

run = True
while run:

    screen.fill(bg_color)
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != "right":
                snake.direction = "left"
                snake.vel = (-snake.step,0)
            elif event.key == pygame.K_RIGHT and snake.direction != "left":
                snake.direction = "right"
                snake.vel = (snake.step,0)
            elif event.key == pygame.K_UP and snake.direction != "down":
                snake.direction = "up"
                snake.vel = (0, -snake.step)
            elif event.key == pygame.K_DOWN and snake.direction != "up":
                snake.direction = "down"
                snake.vel = (0, snake.step)
    
    # update snake pos in every 4th iteration
    timer += 1
    if timer%4 == 0:
        snake.move()
        timer = 0

    # snake eats fruit
    if snake.body[0] == apple.pos:
        snake.eat_fruit()
        score_text.update("Score: "+str(snake.score))
        apple.respawn(w, h)

    # gameover
    for pos in snake.body[1:]:
        if pos == snake.body[0]:
            print("gameover")
            # snake.vel = 0
            # run = False

    snake.draw(screen)
    apple.draw(screen)
    score_text.draw(screen)
    pygame.display.update()


    

