import pygame
from gun import Gun
from bullet import Bullet
 
pygame.init()
 
BLACK = (0,0,0)
WHITE = (255,255,255)

size = (1920, 1080)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shooter")
 
gunA = Gun(BLACK, 100, 10)
gunA.rect.x = 20
gunA.rect.y = 500

bullet = Bullet(BLACK, 100, 100)
bullet.rect.x = 100
bullet.rect.y = 100


all_sprites_list = pygame.sprite.Group()
#all_sprites_list.add(gunA)
all_sprites_list.add(bullet)

carryOn = True

clock = pygame.time.Clock()

while carryOn:

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
              carryOn = False 
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: 
                     carryOn=False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        gunA.moveUp(5)
    if keys[pygame.K_s]:
        gunA.moveDown(5)
    if keys[pygame.K_SPACE]:
        bullet.shoot()

    all_sprites_list.update()

    screen.fill(WHITE)
    
    all_sprites_list.draw(screen) 

    pygame.display.flip()
     

    clock.tick(144)
 

pygame.quit()