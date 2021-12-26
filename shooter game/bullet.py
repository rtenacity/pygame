import pygame
from random import randint
WHITE = (255, 255, 255)
 
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [10, 0]
        
        self.rect = self.image.get_rect()
          
    def update(self):
        self.rect.x += self.velocity[0]

        
   