import pygame
import Knopfklasse

#display fester erstellen
import pygame.math

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TANK-U')

#knopf foto ( hier panzer weil hab knopf noch nicht gemacht)

start_img = pygame.image.load('Pixelart/startknopf.png')
exit_img = pygame.image.load('Pixelart/exitknopf.png')
logo_img = pygame.image.load('Pixelart/Logo-Tank_u-nutzbar-v1.png')


#knopf erstellen [x und y ] position, welches bild, skallierung des bildes

start_knopf = Knopfklasse.knopf(284, 220, start_img, 2.0)
exit_knopf = Knopfklasse.knopf(348, 350, exit_img, 1.0)
logo_img = Knopfklasse.knopf(190, 50, logo_img, 1.5 )


#loop

run = True
while run:

    screen.fill((0, 0, 0))
    logo_img.draw(screen)
#screen wird hier benutzt damit es aus knopf aufgerufen werden kann
    if start_knopf.draw(screen) == True:
        print("Start")
    if exit_knopf.draw(screen) == True:
        print("Exit")
        run = False

    #kümmer sich um das event
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()