# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-05_vertical_movement/src/robot.png")

angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = 320+math.cos(angle)*100-robot.get_width()/2
    y = 240+math.sin(angle)*100-robot.get_height()/2


    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
        
    pygame.display.flip()

    angle += 0.01
    clock.tick(60)