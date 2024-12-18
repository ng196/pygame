import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 800))

# Load graphics
sky = pygame.image.load('graphics/Sky.png')
ground = pygame.image.load('graphics/ground.png')
sky = pygame.transform.scale(sky, (1200, 600)).convert()
ground = pygame.transform.scale(ground, (1200, 200)).convert()
text_font = pygame.font.Font('font/Pixeltype.ttf', 100)

snail = pygame.image.load('graphics/snail/snail1.png')
snail = pygame.transform.scale(snail, (100, 50)).convert_alpha()
snail_x_position = 1190

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # Move the snail and draw everything
    screen.blit(sky, (0, 0))  # Draw sky
    screen.blit(ground, (0, 600))  # Draw ground

    snail_x_position -= 8  # Move the snail to the left
    if snail_x_position < -50 :
        snail_x_position = 1400
    screen.blit(snail, (snail_x_position, 560))  # Draw snail

    pygame.display.update()
    clock.tick(60)
