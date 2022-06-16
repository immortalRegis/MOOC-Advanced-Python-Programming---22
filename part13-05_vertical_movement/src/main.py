# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

screen = pygame.display.set_mode((640,480))

y = 0
y_direction = 1
robot = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-05_vertical_movement/src/robot.png")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0,0,0))
    screen.blit(robot,(0,y))
    pygame.display.flip()

    y += y_direction

    if y_direction > 0 and y + robot.get_height() >= 480:
        y_direction = -y_direction
    if y_direction < 0 and y <= 0:
        y_direction = - y_direction 

    clock.tick(60)