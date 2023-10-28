import pygame, random, math
from pygame.locals import *
from pygame import mixer
pygame.init()
mixer.music.load("Music/Background.mp3") 
mixer.music.set_volume(0.7)
mixer.music.play()
screen     = pygame.display.set_mode((500,600))
running    = True
Clock      = pygame.time.Clock()
dt = 0
gravity = 4 
fired = False
Black = (0,0,0)
bullets_fired = 0
# Positions  of things:
player_pos = pygame.Vector2((0,500))
bullet_pos  = pygame.Vector2((player_pos.x,player_pos.y-20))
enemy_pos = pygame.Vector2()
enemy_pos.x = random.randrange(screen.get_width())
enemy_pos.y = random.randrange(screen.get_height()/2)
#Sprite sheets
sprite_sheet = pygame.image.load('assets/SpaceShooterAssets/SpaceShooterAssetPack_Ships.png').convert_alpha()
sprite_sheet_bullets = pygame.image.load('assets/SpaceShooterAssets/SpaceShooterAssetPack_Projectiles.png').convert_alpha()
bg = pygame.image.load('assets/SpaceShooterAssets/Space Background.png').convert_alpha()
bg_height = bg.get_height()
tiles = math.ceil(screen.get_height() / bg_height)+1
scroll = 0
#Getting images from the sprite sheets
def get_image(sheet,frame,width,height,scale, colour):
    image = pygame.Surface((width,height))
    image.blit(sheet, (0,0),(width*frame,0, width,height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    image.set_colorkey(colour)
    return image
def enemyspawn(x,y):
    screen.blit(enemy_frame_0,(x,y))
    
# Frames:
# 0 is the animation for right , 1 is idel , 2 is left
player_frame_0 = get_image(sprite_sheet,0,8,8,3,Black)
player_frame_1  = get_image(sprite_sheet,1,8,8,3,Black)
player_frame_2  = get_image(sprite_sheet,2,8,8,3,Black)
bullet_frame_1 = get_image(sprite_sheet_bullets,1,8,8,7,Black)
# Enemy
enemy_frame_0 = get_image(sprite_sheet,9,8,8,3,Black)
while running:
    #Scrolling Background
    player_rect = player_frame_0.get_rect(x=(player_pos.x),y=(player_pos.y))
    enemy_rect = enemy_frame_0.get_rect(x=(enemy_pos.x),y=(enemy_pos.y))
    bg_scaled = pygame.transform.scale(bg,(560,600))
    for i in range(0, tiles):
        screen.blit(bg_scaled,(0,i*bg_height-scroll))
    scroll += 1
    if abs(scroll) > bg_height:
        scroll = 0
    # Spawing player,enemys and other 
    collide = pygame.Rect.colliderect(player_rect,enemy_rect)
    # If the objects are colliding
    # then changing the speed direction
    if collide:
        mixer.music.stop() 
        import GameOver
        running = False
    screen.blit(player_frame_1,(player_pos.x,player_pos.y))
    enemyspawn(enemy_pos.x,enemy_pos.y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    #Movement
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        screen.blit(player_frame_0,(player_pos.x,player_pos.y))
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        screen.blit(player_frame_2,(player_pos.x,player_pos.y))
    # Draw Bullets:::
    if keys[pygame.K_f]:
        fired = True
        a=mixer.Sound("Music/Bullet.mp3")
        a.play()
       #Reload
    if keys[pygame.K_r]:
        bullets_fired = 0
    if fired and bullets_fired < 8:
        bullet_rect = bullet_frame_1.get_rect(x=(bullet_pos.x),y=(bullet_pos.y))
        i = 2
        if bullet_rect.colliderect(enemy_rect) and i >1:
            enemy_pos.x = random.randrange(screen.get_width())
            enemy_pos.y = random.randrange(screen.get_height()/2)
        # subtract y valuek causing the bullet to move forward
        bullet_pos.y -= gravity
        screen.blit(bullet_frame_1,(bullet_pos.x,bullet_pos.y))
        # -10 is the y co-ordinate where screen ends  i guess
        if bullet_pos.y < -10:
            fired = False
            bullets_fired = bullets_fired+1
            bullet_pos.y = (player_pos.y-50)
            bullet_pos.x = (player_pos.x)
        if bullet_pos.y > screen.get_height()/2:
            bullet_pos.x = (player_pos.x)
    #Enemy
    enemy_pos.y += gravity
    if enemy_pos.x >= screen.get_width() or enemy_pos.y >= screen.get_height():
        enemy_pos.x = random.randrange(screen.get_width())
        enemy_pos.y = random.randrange(screen.get_height()/2)
    pygame.display.flip()
    dt  = Clock.tick(60) / 1000
pygame.quit()
