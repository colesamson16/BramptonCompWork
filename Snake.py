
import pygame
import os
pygame.init()

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)

gamedisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption('Snake')

leadx = 300
leady = 300

leadxchange = 0
leadychange = 0

clock = pygame.time.Clock()


gameExit = False


while not gameExit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leadxchange = -10

            if event.key == pygame.K_RIGHT:
                leadxchange = 10
            if event.type == pygame.KEYUP:
                leadxchange = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                leadychange = 10

            if event.key == pygame.K_UP:
                leadychange = -10
            if event.type == pygame.KEYUP:
                leadxchange = 0



    leadx += leadxchange
    leady += leadychange
    gamedisplay.fill(black)
    pygame.draw.rect(gamedisplay, green, [leadx, leady, 10, 10])

    clock.tick(30)
    pygame.display.update()