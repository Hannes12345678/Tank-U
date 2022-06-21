import pygame
from tank_Network import Network
from Panzerbwegung import Player
#gegege
width = 1001
height = 501
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
blauer_panzer = pygame.image.load("Blue-Tank-V1.png")
roter_panzer =pygame.image.load("red-tank-v1-benutzen.png")
blaues_hartes_ding = pygame.image.load("Blue-tank-Kanone-v1-nutzen.png")
blaues_hartes_ding.set_colorkey((255,255,255))
rotes_hartes_ding = pygame.image.load("red-tank-kanone-v1-nutzen.png")
blaues_hartes_ding_turned = pygame.image.load("Blue-Kanone-turned.png")
rotes_hartes_ding_turned = pygame.image.load("red-Kanone-turned.png")
hinter_grundussus = pygame.image.load('hintergrund.png')

def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    win.blit(hinter_grundussus,(0,0))

    player.draw(win)
    player2.draw(win)


    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    t = n.getP()
    clock = pygame.time.Clock()

    barrelrotation = 0
    while run:
        clock.tick(20)  #30 fps kamen von Konrad und Hannes deshalb ok wenn die Idee von Willi käme dann hätten wäre es fatal und falsch
        p2 = n.send(p)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.tank_move()


        print(p)
        print(p2)
        print(p.x)
        print(p.y)
        print(p2.x)
        print(p2.y)
        redrawWindow(win, p, p2)
        blaueshartesding = pygame.transform.rotate(blaues_hartes_ding, barrelrotation)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            barrelrotation = barrelrotation -5

        if keys[pygame.K_DOWN]:
            barrelrotation = barrelrotation +5




        win.blit(blaueshartesding, ( p.x + 45 - int(blaueshartesding.get_width() / 2), p.y + 80 - int(blaueshartesding.get_height() / 2)))


        win.blit(rotes_hartes_ding_turned, (p2.x + 15, p2.y +75))
        win.blit(roter_panzer, (p2.x, p2.y))
        win.blit(blauer_panzer, (p.x, p.y))


        pygame.display.update()
#main() habe es in kommentar gesetzt damit man bei ui testen kann