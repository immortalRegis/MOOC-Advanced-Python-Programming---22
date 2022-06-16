# WRITE YOUR SOLUTION HERE:

import math
import pygame
from random import randint

pygame.init()

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Asteroid')
robot = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-05_vertical_movement/src/robot.png")
rock = pygame.image.load("C:/Users/user/AppData/Local/tmc/vscode/mooc-programming-22/part13-17_asteroids/src/rock.png")

def collision_occurs(objectx, objecty, robotx, roboty):
    x_distance = objectx-robotx
    y_distance = objecty - roboty

    x_distance *= x_distance
    y_distance *= y_distance

    distance_in_pixels = math.sqrt(x_distance + y_distance)
    return distance_in_pixels < 40


x = 0
y = height - robot.get_height()
points = 0

to_left = False
to_right = False

game_font = pygame.font.SysFont("Arial", 24)
text = game_font.render("Points: " + str(points), True, (255, 0, 0))

asteroids = []

for i in range(5):
    asteroids.append([randint(0, width - rock.get_width()), -randint(100, 200)])

game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            
    if game_over:
        text = game_font.render(f"Game Over! You scored {points} points", True, (255, 0, 0))
        screen.blit(text, (320, 240))
        pygame.display.flip()
    else:            
        for i in range(5):
            if asteroids[i][1]+rock.get_height() < height:
                asteroids[i][1] += 1
                if collision_occurs(asteroids[i][0], asteroids[i][1], x, y):
                    points += 1
                    asteroids[i][0] = randint(0,width-rock.get_width())
                    asteroids[i][1] = -randint(100,1000)
            else:
                game_over = True
                asteroids[i][0] = randint(0,width-rock.get_width())
                asteroids[i][1] = -randint(100,1000)
                
                
        

        if to_right and (x + 2) + robot.get_width() <= width:
            x += 2
        if to_left and (x - 2) >= 0:
            x -= 2

        screen.fill((0,0,0))

        for i in range(5):
            screen.blit(rock, (asteroids[i][0], asteroids[i][1]))
        
        text = game_font.render("Points: " + str(points), True, (255, 0, 0))
        screen.blit(text, (500, 10))
        screen.blit(robot, (x,y))
        pygame.display.flip()
        clock = pygame.time.Clock().tick(60)



    


    
