import pygame,math,os
from pygame import mixer
pygame.init()
mixer.init()
mixer.music.load("Music/Title screen.ogg") 
mixer.music.set_volume(0.7)
mixer.music.play()
screen = pygame.display.set_mode((500,600))
start = pygame.image.load("assets/SpaceShooterAssets/Start.png")
sta = pygame.transform.scale(start,(400,300))
sta_rect = sta.get_rect(x=(100),y=(200))
stop = pygame.image.load("assets/SpaceShooterAssets/buttons-quit.png")
qui = pygame.transform.scale(stop,(300,200))
qui_rect = qui.get_rect(x=(150),y=(300))
title = pygame.image.load("assets/SpaceShooterAssets/Title.png")
bg     = pygame.image.load("assets/SpaceShooterAssets/Space Background.png")
bg_height = bg.get_height()
title_scaled = pygame.transform.scale(title,(600,400))
bg_scaled = pygame.transform.scale(bg,(560,600))
tiles = math.ceil(screen.get_height() / bg_height)+1
scroll = 0
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    for i in range(0,tiles):
        screen.blit(bg_scaled,(0,i*bg_height-scroll))
    scroll += 1
    if abs(scroll) > bg_height:
        scroll = 0
    screen.blit(title_scaled, (5,80))
    screen.blit(qui,(150,300))
    screen.blit(sta,(100,200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if qui_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        if sta_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                mixer.music.stop()
                import main
                running = False
    pygame.display.flip()
pygame.quit()