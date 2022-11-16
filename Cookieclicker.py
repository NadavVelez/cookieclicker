
import pygame


import os

cwd = os.getcwd()

cookiesperclick = 1
cookiespersec = 0
cookies = 0

pygame.init()

gamedisplay = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Cookie Clicker')
cookie = pygame.image.load(os.path.join(cwd,'Cookie.png'))
cookieRec = cookie.get_rect()
powerup = pygame.image.load(os.path.join(cwd,'Supermushroom.png'))
powerup = pygame.transform.scale(powerup,(100,100))
powerRec = powerup.get_rect()
powerRec.x = 255
clicks = 0
mushroomclicks = 0


gamedisplay.fill((255,255,255))
gamedisplay.blit(cookie,cookieRec)
gamedisplay.blit(powerup,powerRec)
pygame.display.update()
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if cookieRec.collidepoint(pos):
                clicks += cookiesperclick
                print(clicks)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if powerRec.collidepoint(pos):
                mushroomclicks += 1
                print(mushroomclicks)




pygame.quit
