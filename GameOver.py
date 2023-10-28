import pygame
from pygame import mixer
pygame.init()
mixer.init()
mixer.music.load("Music/GameOver.ogg") 
mixer.music.set_volume(0.7)
mixer.music.play()
screen = pygame.display.set_mode((500,600))
bg = pygame.image.load("assets/SpaceShooterAssets/Space Background-Blurred.png").convert_alpha()
button_img_restart =  pygame.image.load("assets/SpaceShooterAssets/buttons-restart.png").convert_alpha()
button_img_quit =  pygame.image.load("assets/SpaceShooterAssets/buttons-quit.png").convert_alpha()
restart = pygame.transform.scale(button_img_restart,(300,240))
stop = pygame.transform.scale(button_img_quit,(300,200))
button_img_quit_rect = stop.get_rect(x=(150),y=(300))
button_img_restart_rect = restart.get_rect(x=(100),y=(50))
bg_scaled = pygame.transform.scale(bg,(560,600))
running = True
while running:
    mouse_pos=  pygame.mouse.get_pos()
    screen.blit(bg_scaled,(0,0))

    screen.blit(stop,(150,300))
    screen.blit(restart,(100,200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if button_img_quit_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                running =False
        if button_img_restart_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                mixer.music.stop()
                import main
                running = False
    pygame.display.flip()
pygame.quit()