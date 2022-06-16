# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-05_vertical_movement/src/robot.png")

x = 0
y = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]

            if mouse_x >= x and mouse_x <= (x + robot.get_width()):
                x = randint(0, 640 - robot.get_width())
                y = randint(0, 480 - robot.get_height())
                
        screen.fill((0,0,0))
        screen.blit(robot, (x, y))
        pygame.display.flip()

        if event.type == pygame.QUIT:
            exit()
