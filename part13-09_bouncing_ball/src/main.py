# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

ball = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-09_bouncing_ball/src/ball.png")

x = 0
y = 0

x_dir = 1
y_dir = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    screen.fill((0,0,0))
    screen.blit(ball, (x,y))

    x += x_dir
    y += y_dir

    if x == 0 or x + ball.get_width() == 640:
        x_dir = -x_dir
    if y == 0 or y + ball.get_height() == 480:
        y_dir = -y_dir
    
        
     
    pygame.display.flip()

    clock.tick(60)