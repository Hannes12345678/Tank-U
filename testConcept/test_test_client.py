import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("TANK-U / Prototyp-Movement")
clock = pygame.time.Clock()
FPS = 60 # sollte fix so bleiben

sky_surface = pygame.image.load('übungs-texturen Kopie/Sky.png')
ground_surface =

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface, (0,0))

    pygame.display.update()
    clock.tick(FPS)

