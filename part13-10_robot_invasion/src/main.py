# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
robot = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-05_vertical_movement/src/robot.png")
clock = pygame.time.Clock()

robots = []
for i in range(5):
    robots.append([randint(0, width - robot.get_width()), -randint(100, 150)])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for i in range(len(robots)):
        if robots[i][1] < height - robot.get_height():
            robots[i][1] += 1
        else:
            if robots[i][0] < -robot.get_width() or robots[i][0] > width:
                robots[i][0] = randint(0, width - robot.get_width())
                robots[i][1] = -randint(100, 300)
            elif robots[i][0]+robot.get_width() < width/2:
                robots[i][0] -= 1
            else:
                robots[i][0] += 1
    
    screen.fill((0,0,0))

    for i in range(len(robots)):
        screen.blit(robot, (robots[i][0], robots[i][1]))
    
    pygame.display.flip()
    clock.tick(60)