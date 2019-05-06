import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Stand and Play!')
gameDisplay.fill(red)
pygame.display.update()

running = True

while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gameDisplay.fill(white)

    pygame.draw.rect(gameDisplay, red,[WIDTH/10,HEIGHT/3,WIDTH/5,HEIGHT/3])
    pygame.draw.rect(gameDisplay, red,[(WIDTH - 0.4 * WIDTH),HEIGHT/3,WIDTH/5,HEIGHT/3])
    pygame.display.update()


pygame.quit()
