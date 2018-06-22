
import pygame, sys

from pygame.locals import *

pygame.init()

tilesize = 160
mapwidth = 3
mapheight = 5

gameDisplay = pygame.display.set_mode((mapwidth*tilesize,mapheight*tilesize), pygame.)

dirt = 0
grass = 1
water = 2
coal = 3

black = (0,0,0)
brown = (153,76,0)
green = (0,255,0)
blue = (0,0,255)

colours = {
    dirt:brown,
    grass:green,
    water:blue,
    coal:black
}



tilemap = [
    [grass,coal,dirt],
    [water,water,grass],
    [coal,grass,water],
    [dirt,grass,coal],
    [grass,water,dirt]
]

textures = {
    dirt: pygame.image.load('dirt.png'),
    grass: pygame.image.load('grass.png'),
    water: pygame.image.load('water.png'),
    coal: pygame.image.load('coal.png')
}


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for row in range(mapheight):
        for column in range (mapwidth):
            pygame.draw.rect(gameDisplay,colours[tilemap[row][column]],(column*tilesize,row*tilesize,tilesize,tilesize))

    pygame.display.update()




