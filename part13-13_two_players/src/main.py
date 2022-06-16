# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot1 = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-05_vertical_movement/src/robot.png")
robot2 = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-05_vertical_movement/src/robot.png")


x = 320
y = 240

x2 = 200
y2 = 200

to_right = False
to_left = False
move_up = False
move_down = False

to_right2 = False
to_left2 = False
move_up2 = False
move_down2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

            if event.key == pygame.K_a:
                to_left2 = True
            if event.key == pygame.K_d:
                to_right2 = True
            if event.key == pygame.K_w:
                move_up2 = True
            if event.key == pygame.K_s:
                move_down2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False
            
            if event.key == pygame.K_a:
                to_left2 = False
            if event.key == pygame.K_d:
                to_right2 = False
            if event.key == pygame.K_w:
                move_up2 = False
            if event.key == pygame.K_s:
                move_down2 = False

        if event.type == pygame.QUIT:
            exit()

    if to_right and (x + 2) + robot1.get_width() <= 640:
        x += 2
    if to_left and (x - 2) >= 0:
        x -= 2
    if move_up and (y - 2)>= 0:
        y -= 2
    if move_down and (y + 2) + robot1.get_height() <= 480:
        y += 2


    if to_right2 and (x2 + 2) + robot2.get_width() <= 640:
        x2 += 2
    if to_left2 and (x2 - 2) >= 0:
        x2 -= 2
    if move_up2 and (y2 - 2)>= 0:
        y2 -= 2
    if move_down2 and (y2 + 2) + robot2.get_height() <= 480:
        y2 += 2

    window.fill((0, 0, 0))
    window.blit(robot1, (x, y))
    window.blit(robot2, (x2, y2))
    pygame.display.flip()

    clock.tick(60)