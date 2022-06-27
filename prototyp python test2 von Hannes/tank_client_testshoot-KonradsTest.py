import pygame
from tank_Network import Network
from Panzerbwegung import *
import pygame
import Knopfklasse
import pygame.math
from math import pi
from math import cos
from math import sin

#gegege
#keys = pygame.key.get_pressed()

n = Network()
p = n.getP()
t = n.getP()
#bullet variablen (können später gemacht werden )
bullety = p.y
bulletx = p.x

shustark = 10

bullet_state = False
bullet_shoot = False


g = [0, -10, 0]
v0 = 10
theta = int(30 * pi / 180)
r = [0, 0, 0]
v = int(v0)*[int(cos(theta)),int( sin(theta)), 0]
m = int(1)
pos = m * v
time = 0
dtime = 1 #maybe was anderes

F = m*g

stearke = 0





#muss wurf distanz berechnen



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
runde_kugel = pygame.image.load('bullet.png')
hinter_grundussus = pygame.image.load('hintergrund.png')



bullet_group = pygame.sprite.Group()



#display fester erstellen
import pygame.math
#jjjj
SCREEN_HEIGHT = height
SCREEN_WIDTH = width
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
""" 
#########################################################################################
Gerade gibt es starke performance probleme mit der schießmechanik vllt 
liegt es an meinem Laptop, egal. - K


Notiz an mich selbst : 
vllt sollte ich den code unten hinein machen und auf globale variablen 
verzichten und dafür locale ausprobieren... 

oder den alten code so modifizieren das er mit y funkt und man kann 4 
stärke einstellungen machen  1, 2, 3 ,4 -> mit den nummern und dann kommt 
eine bestimmte weite mit vllt etwas randomness 
aber wäre dann auch einfach die turrets damit zu verbinden 
oder gleich panzer neu designen 

!!!! auf jedenfall den alten code nutzen den mit der neue idee inspiriert über arbeiten 

##########################################################################################
"""


#logic des schießens
def fire_bullet(x,y):
    global bullet_shoot
    global bullet_state
    global g
    global v0
    global theta
    global r
    global v
    global m
    global pos
    global time
    global dtime
    global F
    global stearke

    global shustark
    keys = pygame.key.get_pressed()

    bullet_state = True
    bullet_shoot = True
    while bullet_shoot:
        print(shustark)
        if keys[pygame.K_w]:
            print('w')
            shustark = shustark + 20           # bestimmt die schuss stärken weite
        elif keys[pygame.K_s]:
            print('s')
            shustark =shustark - 20
        elif keys[pygame.K_e]:
            print('shooting preparation')
            xbh = 0
            ybh = 0
            shushalb = shustark /2
            rotation = 0
            for x in range(shustark):

                win.blit(runde_kugel,(x + xbh  , y + ybh) )
                xbh = xbh +10
                rotation = rotation + 1

                if rotation < shustark:
                  ybh = ybh - 5
                else:
                    ybh = ybh + 5
            bullet_shoot = False
        if y > 600:
            bullet_shoot = False

def stop_bullet():
    global bullet_state
    bullet_state = False

#kugel stärke

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
    """n = Network()
    p = n.getP()  #ist jetzt oben drinn muss was überprüfen 
    t = n.getP()"""
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
        """bullety = p.y
        bulletx = p.x"""







        if p.id == "Player 1":
            win.blit(roter_panzer, (p2.x, p2.y))
            win.blit(blauer_panzer, (p.x, p.y))

        if p.id == "Player 2":
            win.blit(roter_panzer, (p.x, p.y ))
            win.blit(blauer_panzer, (p2.x, p2.y))






        if p.id == "Player 1":
            blaueshartesding = pygame.transform.rotate(blaues_hartes_ding_turned, barrelrotation)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP] and barrelrotation <= 230:
                barrelrotation = barrelrotation + 5

            if keys[pygame.K_DOWN] and barrelrotation >= 180:
                barrelrotation = barrelrotation - 5

            win.blit(blaueshartesding, (p.x + 85- int(blaueshartesding.get_width() / 2), p.y + 75  - int(blaueshartesding.get_height() / 2)))

            win.blit(rotes_hartes_ding_turned, (p2.x + 15, p2.y + 75 ))
            #print(barrelrotation)
#hier shooting mech p1
           # if keys[pygame.K_w]:


            if keys[pygame.K_SPACE]:
                print('Hello i am under the water')


                fire_bullet(p.x , p.y )

            """if bullet_state is True:
                 variX = 0
                 bulletx = p.x + 20
                 bullet_shoot = True

                 while bullet_shoot:   #while variX < 900 V1.0 schuss geht gerade aus
                     variX = variX + 10
                     fire_bullet(bulletx + variX, p.y)
                     if variX > 900:
                         bullet_shoot = False
                         stop_bullet()"""













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




run = True
while run:

    screen.fill((0, 0, 0))
    logo_img.draw(screen)
#screen wird hier benutzt damit es aus knopf aufgerufen werden kann
    if start_knopf.draw(screen) == True:
        print("Start")

        main()
        #startet den client

#ggg



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