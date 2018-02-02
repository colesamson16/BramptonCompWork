import pygame
pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
gamedisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('slither')

gameexit = False
lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0
clock = pygame.time.Clock()

while not gameexit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameexit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                lead_y_change = -10

    lead_x += lead_x_change
    lead_y += lead_y_change
    gamedisplay.fill(white)
    snakelen = pygame.draw.rect(gamedisplay, green, [lead_x,lead_y,10,10])
    pygame.display.update()

    clock.tick(30)
pygame.quit()
quit()