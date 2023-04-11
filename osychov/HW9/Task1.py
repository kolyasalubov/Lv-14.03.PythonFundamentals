import pygame
import random

pygame.init()
gameDisplay = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
    pygame.display.update()
    clock.tick(60) 
