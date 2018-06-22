import pygame
import random

w = 360
h = 480
fps = 360

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

pygame.init()

screen = pygame.display.set_mode((w,h), pygame.RESIZABLE)
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()

pygame.quit()
quit()
