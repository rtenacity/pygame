import pygame
from gun import Gun
from bullet import Bullet
from target import Target
import time
import math
from random import randint

pygame.init()
 
BLACK = (0,0,0)
WHITE = (255,255,255)

size = (1000, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Shooter")
 
gunA = Gun(BLACK, 70, 50)
gunA.rect.x = 25
gunA.rect.y = 220

target = Target(BLACK, 10, 50)
target.rect.x = 950
target.rect.y = 220

bullet = Bullet(BLACK, 10, 10)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(gunA)
all_sprites_list.add(target)

carryOn = True

x = 1

score = 0

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
    if event.type == pygame.MOUSEBUTTONDOWN:
        bullet = Bullet(BLACK, 10, 10)
        bullet.rect.x = gunA.rect.x
        bullet.rect.y = gunA.rect.y
        all_sprites_list.add(bullet) 
        time.sleep(0.05)
    
    if pygame.sprite.collide_rect(bullet, target):
       print("hello" + str(x))
       x+=1
       score+=1
       target.rect.y = randint(50, 450)

    font = pygame.font.Font(None, 74)
    text = font.render(str(score), 1, WHITE)
    screen.blit(text, (250,10))

    all_sprites_list.update()
    screen.fill(WHITE)
    all_sprites_list.draw(screen) 

    pygame.display.flip()
     

    clock.tick(144)
 

pygame.quit()