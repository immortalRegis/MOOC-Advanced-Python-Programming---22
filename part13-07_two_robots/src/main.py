# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))
x1 = 0
x2 = 2

y1 = 0
y2 = 100

x1_vel = 1
x2_vel = 2

robot1 = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-05_vertical_movement/src/robot.png")
robot2 = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-05_vertical_movement/src/robot.png")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    screen.fill((0,0,0))
    screen.blit(robot1,(x1, y1))
    screen.blit(robot2,(x2, y2))

    pygame.display.flip()

    x1 += x1_vel
    if x1_vel > 0 and x1 + robot1.get_width() >= 640:
        x1_vel = -x1_vel
    if x1_vel < 0 and x1 <= 0:
        x1_vel = -x1_vel
    clock.tick(60)

    x2 += x2_vel
    if x2_vel > 0 and x2 + robot2.get_width() >= 640:
        x2_vel = -x2_vel
    if x2_vel < 0 and x2 <= 0:
        x2_vel = -x2_vel
    clock.tick(120)