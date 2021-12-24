# Import and initialize the pygame library
import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_c,
    QUIT,
)

pygame.init()
x = 250
y = 250
color_change = 255
# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_UP:
                y = y - 5
            if event.key == K_DOWN:
                y = y + 5
            if event.key == K_LEFT:
                x = x - 5
            if event.key == K_RIGHT:
                x = x + 5
            if event.key == K_c:
                color_change = color_change - 10
            



    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.rect(screen, (0, 0, color_change), pygame.Rect(x, y, 100, 100))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()