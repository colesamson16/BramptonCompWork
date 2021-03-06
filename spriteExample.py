#pygame template

import pygame
import random
import os

width = 720
height = 480
fps = 30

#define colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#set up assets folders
gameFolder = os.path.dirname(__file__)
imgFolder = os.path.join(gameFolder,"imgtut")

class Player(pygame.sprite.Sprite):
    #sprite for player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(imgFolder, 'p1_jump.png')).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,height/2)
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > height - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > width:
            self.rect.right = 0

#init pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()

allSprites = pygame.sprite.Group()
player = Player()
allSprites.add(player)


#game loop
running = True
while running:
    #keep loop running at right speed
    clock.tick(30)
    #process input
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False

    #update
    allSprites.update()

    #draw/render
    screen.fill(blue)
    allSprites.draw(screen)
    pygame.display.update()
