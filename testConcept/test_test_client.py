import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("TANK-U / Prototyp-Movement")
clock = pygame.time.Clock()
FPS = 60 # sollte fix so bleiben
test_font = pygame.font.Font('übungs-texturen Kopie/Font/Pixeltype.ttf', 50 )

sky_surface = pygame.image.load('übungs-texturen Kopie/Sky.png')
ground_surface = pygame.image.load('übungs-texturen Kopie/ground.png')
text_surface = test_font.render('Mygame', False, 'Black')

snail_surface = pygame.image.load('übungs-texturen Kopie/Snail/snail1.png')
snail_x_pos = 600
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface,(0,300) )
    screen.blit(text_surface,(300,50))
    if snail_x_pos >= -100 :
        snail_x_pos -= 3
    else:
        snail_x_pos = 900

    screen.blit(snail_surface,(snail_x_pos,264 ))

    pygame.display.update()
    clock.tick(FPS)

