#pygame template

import pygame
import random

width = 360
height = 480
fps = 30

#define colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class Player(pygame.sprite.Sprite):
    #sprite for player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,height/2)

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > width:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

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
    screen.fill(black)
    allSprites.draw(screen)
    pygame.display.update()
