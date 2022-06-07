import os.path

import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("game 1")
WHITE = (255, 255, 255)
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 128, 128
PURPLE_SPACESHIP_IMAGE = pygame.image.load('bilderhehe/purple_ship.png')
PURPLE_SPACESHIP = pygame.transform.scale(PURPLE_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
GREE_SPACESHIP_IMAGE = pygame.image.load('bilderhehe/green_ship.png')
GREE_SPACESHIP = pygame.transform.scale(GREE_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))


def draw_window():
    WIN.fill(WHITE)
    WIN.blit(PURPLE_SPACESHIP, (100, 250))
    WIN.blit(GREE_SPACESHIP, ( 700, 250))
    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    run = True
    while run == True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()

#if __name__ == "__haupt__":

main()


