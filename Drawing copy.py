import math
import random
from typing import Text
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CORAL = (255, 127, 80)
LIME = (50, 205, 50)
CYAN = (0, 255, 255)
GRASS= (118, 142, 73)
PI = 3.141592653
YELLOW= (255, 255, 0)
SUNRAY= (246, 217, 65)
BALLON= (103, 78, 167)
SWORD= (172, 168, 168)
CLOUD= (228, 244, 247)
NIGHT= (22, 83, 126)


pygame.init()

size = (1000, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Denis' very cool game")
done = False
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here


    screen.fill(NIGHT)

    # --- Drawing code should go here    
    pygame.draw.rect(screen, LIME, [0, 0, 1000, 500], 5)
    

    pygame.draw.ellipse(screen, CLOUD, [120,60,240,90], 50)
    pygame.draw.ellipse(screen, CLOUD, [140,40,200,110], 50)


    pygame.draw.rect(screen, GRASS, [5, 490, 995, 480], 10)
    pygame.draw.circle(screen, YELLOW, [1000, 0], 100)
    pygame.draw.line(screen, SUNRAY, [900, 20],[820, 60], 5)
    pygame.draw.line(screen, SUNRAY, [900, 20],[820, 0], 5)
    pygame.draw.line(screen, SUNRAY, [920, 60],[820, 60], 5)
    pygame.draw.line(screen, SUNRAY, [920, 60],[850, 120], 5)
    pygame.draw.line(screen, SUNRAY, [960, 90],[850, 120], 5)
    pygame.draw.line(screen, SUNRAY, [960, 90],[900, 170], 5)
    pygame.draw.line(screen, SUNRAY, [1000, 100],[900, 170], 5)

    
    font = pygame.font.SysFont('New Times Roman', 25, False, False)
    text = font.render("Welcome To StickWorldV1",True,RED)
    screen.blit(text, [350, 220])
    
    for x_offset in range(0, 900, 300):
        pygame.draw.line(screen, CORAL, [65+x_offset, 440], [75+x_offset, 300], 1)
        pygame.draw.circle(screen, BALLON, [75+x_offset, 300], 30)

    for x_offset in range(0, 900, 300): 
            
        pygame.draw.line(screen, RED, [45+x_offset, 470], [45+x_offset, 400], 2)
        pygame.draw.circle(screen, RED, [45+x_offset, 390], 15)
        pygame.draw.line(screen, RED, [45+x_offset, 410],[60+x_offset, 440], 2)
        pygame.draw.line(screen, RED, [45+x_offset, 410],[30+x_offset, 440], 2)
        pygame.draw.line(screen, RED, [45+x_offset, 470],[60+x_offset, 480], 2)
        pygame.draw.line(screen, RED, [45+x_offset, 470],[30+x_offset, 480], 2)
        
    pygame.display.flip()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)


    
# Close the window and quit.
pygame.quit()

