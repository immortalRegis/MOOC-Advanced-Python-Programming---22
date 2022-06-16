# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((750, 480))

robot = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-05_vertical_movement/src/robot.png")

width = robot.get_width()
row_start_point = (640 - (10 * width))/2
start_point = row_start_point

height = 150

window.fill((0, 0, 0))

for j in range(10):
    for i in range(10):
        window.blit(robot, (start_point, height))
        start_point += width
    row_start_point += 20
    start_point = row_start_point
    height += 20
    
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()