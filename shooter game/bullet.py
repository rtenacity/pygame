import pygame
from random import randint
WHITE = (255, 255, 255)
 
class Bullet(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [10, 0]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
          
    def update(self):
        self.rect.x += self.velocity[0]

        
   