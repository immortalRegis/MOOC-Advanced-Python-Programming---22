# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-05_vertical_movement/src/robot.png")

window.fill((0, 0, 0))

for i in range(1000):
    window.blit(robot, (randint(0, 640), randint(0, 480)))  

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()