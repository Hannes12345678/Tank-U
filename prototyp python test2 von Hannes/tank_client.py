import pygame
from tank_Network import Network
from Panzerbwegung import *
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


bullet_group = pygame.sprite.Group()

"""class Bullegame():
    def create_bullet(self, x, y):    #hab autismuss teste hier was 
        self.x = x
        self.y = y
        return Bullet(self.x + 10, self.y + 10)


class Bullet(pygame.sprite.Sprite):
    # hier wird ein neuer würfel für die bullets gemacht
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.rect(x, y)

    def update(self):
        self.rect.x += 5"""







def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    win.blit(hinter_grundussus,(0,0))

    player.draw(win)
    player2.draw(win)
    bullet_group.draw(win)
    bullet_group.draw(win)


    pygame.display.update()



#ddd
def main():
    run = True
    n = Network()
    p = n.getP()
    t = n.getP()
    clock = pygame.time.Clock()

    barrelrotation = 180
    while run:
        clock.tick(20)  #30 fps kamen von Konrad und Hannes deshalb ok wenn die Idee von Willi käme dann hätten wäre es fatal und falsch
        p2 = n.send(p)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.tank_move()


        #print(p)
        #print(p2)
        print(p.x)
        #print(p.y)
        #print(p2.x)
        #print(p2.y)
        redrawWindow(win, p, p2)







        if p.id == "Player 1":
            win.blit(roter_panzer, (p2.x, p2.y + 116))
            win.blit(blauer_panzer, (p.x, p.y + 120))

        if p.id == "Player 2":
            win.blit(roter_panzer, (p.x, p.y + 116))
            win.blit(blauer_panzer, (p2.x, p2.y + 120))


        if p.id == "Player 1":
            blaueshartesding = pygame.transform.rotate(blaues_hartes_ding_turned, barrelrotation)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP] and barrelrotation <= 230:
                barrelrotation = barrelrotation + 5

            if keys[pygame.K_DOWN] and barrelrotation >= 180:
                barrelrotation = barrelrotation - 5

            win.blit(blaueshartesding, (p.x + 85- int(blaueshartesding.get_width() / 2), p.y + 75 + 120 - int(blaueshartesding.get_height() / 2)))

            win.blit(rotes_hartes_ding_turned, (p2.x + 15, p2.y + 75 + 116))
            #print(barrelrotation)

            if keys[pygame.K_SPACE]:
              print('Hello i am under the water')


            """ bullet_group.add(Bullegame.create_bullet(p.x, p.y)) """



        if p.id == "Player 2":

            roteshartesding = pygame.transform.rotate(rotes_hartes_ding, barrelrotation)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP] and barrelrotation > 120:
                barrelrotation = barrelrotation - 5

            if keys[pygame.K_DOWN] and barrelrotation <= 180:
                barrelrotation = barrelrotation + 5

            win.blit(blaues_hartes_ding,(p2.x+ 20 , p2.y +120))
            win.blit(roteshartesding, (p.x +35 - int(roteshartesding.get_width() / 2), p.y + 90 + 116 - int(roteshartesding.get_height() / 2)))
            #print(barrelrotation)
        pygame.display.update()
#main() habe es in kommentar gesetzt damit man bei ui testen kann