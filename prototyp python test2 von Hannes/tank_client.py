import pygame
from tank_Network import Network
from Panzerbwegung import Player

width = 1000
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
blauer_panzer = pygame.image.load("Blue-Tank-V1.png")
roter_panzer =pygame.image.load("red-tank-v1-benutzen.png")
blaues_hartes_ding = pygame.image.load("Blue-tank-Kanone-v1-nutzen.png")
rotes_hartes_ding = pygame.image.load("red-tank-kanone-v1-nutzen.png")
blaues_hartes_ding_turned = pygame.image.load("Blue-Kanone-turned.png")
rotes_hartes_ding_turned = pygame.image.load("red-Kanone-turned.png")


def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))

    player.draw(win)
    player2.draw(win)


    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)  #30 fps kamen von Konrad und Hannes deshalb ok wenn die Idee von Willi käme dann hätten wäre es fatal und falsch
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
        win.blit(blaues_hartes_ding, (p.x + 15 , p.y ))
        win.blit(rotes_hartes_ding_turned, (p2.x + 15, p2.y +75))
        win.blit(roter_panzer, (p2.x, p2.y))
        win.blit(blauer_panzer, (p.x, p.y))


        pygame.display.update()
main()