from superwires import games
import pygame
import math 
import random


class run():
    img = pygame.image.load("mars.jpg")
    background_colour = (255,0,0)
    (width, height) = (600, 500)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tutorial 1')
    #Show background picture 
    screen.blit(img,(0,0)) 
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
































