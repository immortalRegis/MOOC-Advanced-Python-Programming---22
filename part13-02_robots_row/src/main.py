# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-05_vertical_movement/src/robot.png")

width = robot.get_width()
start_point = (640 - (10 * width))/2

window.fill((0, 0, 0))

for i in range(10):
    window.blit(robot, (start_point, 150))
    start_point += width
    
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()