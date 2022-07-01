import pygame
from tank_Network import Network
from Panzerbwegung import *
import pygame
import Knopfklasse
import pygame.math
from math import pi
from math import cos
from math import sin
#ijijijij
#gegege

n = Network()
p = n.getP()
t = n.getP()
#bullet variablen (können später gemacht werden )
bullety = p.y
bulletx = p.x
bullet_staerke = 15 # hier immer ungerade
bullet_winkel = 0 # davor 10

faky = 5  # faktoren der fariabelnen für x und
fakx = 5


bullet_state = False
bullet_shoot = False

g = [0, -9.8, 0]
v0 = 10
theta = 30 * pi / 180
r = [0,0,0]
v = v0*[cos(theta), sin(theta), 0]
m = 1
pos = m * v
time = 0
dtime = 0.01 #maybe was anderes









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



#logic des schießens
def fire_bullet(x,y):
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

    bullet_state = True
   # while y < 501 :
    win.blit(runde_kugel,(x+90  , y+55) )

def fire_bulletP2(x,y):
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

    bullet_state = True
   # while y < 501 :
    win.blit(runde_kugel,(x+90  , y+55) ) # muss geändert werden
def stop_bullet():
    global bullet_state
    bullet_state = False
    #print("aufhören")

def stop_bulletP2():
    global bullet_state
    bullet_state = False
    #print("aufhören")

def bullet_weite():
    global bullet_staerke
    bullet_staerke = bullet_staerke + 2



    sxs = 250
    if bullet_staerke > sxs:
        bullet_staerke = bullet_staerke - 2

def bullet_weiteP2():
    global bullet_staerke
    bullet_staerke = bullet_staerke + 2
    sxs = 250
    if bullet_staerke > sxs:
        bullet_staerke = bullet_staerke - 2

def bullet_kurz():
    global bullet_staerke
    bullet_staerke = bullet_staerke - 2

    sxs = 250
    if bullet_staerke > sxs:
        bullet_staerke = bullet_staerke - 2

    if bullet_staerke < 5:
        bullet_staerke = bullet_staerke + 2


def bullet_kurzP2():
    global bullet_staerke
    bullet_staerke = bullet_staerke - 2

    sxs = 250
    if bullet_staerke > sxs:
        bullet_staerke = bullet_staerke - 2

    if bullet_staerke < 5:
        bullet_staerke = bullet_staerke + 2
def bullet_grad_plus():
    global bullet_winkel
    global fakx
    global faky
    bullet_winkel = bullet_winkel + 3

    if bullet_winkel < 18 and faky <= 18:
        faky = faky + 3
        if fakx > 2:
            fakx = fakx - 3
        elif fakx > 18:
            fakx = 5
            faky = 5
        else:
            fakx = fakx + 3
def bullet_grad_plusP2():
    global bullet_winkel
    global fakx
    global faky
    bullet_winkel = bullet_winkel + 3

    if bullet_winkel < 18 and faky <= 18:
        faky = faky + 3
        if fakx > 2:
            fakx = fakx - 3
        elif fakx > 18:
            fakx = 5
            faky = 5
        else:
            fakx = fakx + 3
def bullet_grad_minus():
    global bullet_winkel
    global fakx
    global faky
    bullet_winkel = bullet_winkel - 3
    if bullet_winkel > 0 and fakx <= 18:
        fakx = fakx + 3
        if faky > -1:
            faky = faky - 3
        elif fakx >18:
            fakx = 5
            faky = 5
        else:
            faky = faky + 3
def bullet_grad_minusP2():
    global bullet_winkel
    global fakx
    global faky
    bullet_winkel = bullet_winkel - 3
    if bullet_winkel > 0 and fakx <= 18:
        fakx = fakx + 3
        if faky > -1:
            faky = faky - 3
        elif fakx >18:
            fakx = 5
            faky = 5
        else:
            faky = faky + 3


def reset_bullet_trajectory():
    global fakx
    global faky
    global bullet_winkel
    fakx = 5
    faky = 5
    bullet_winkel =0

def reset_bullet_trajectoryP2():
    global fakx
    global faky
    global bullet_winkel
    fakx = 5
    faky = 5
    bullet_winkel =0

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

    barrelrotation = 230
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
        #print(p.x)
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
            barrelrotation = 230


            variX = 0 #wie stark das zeug ist bzw winkel
            variY = 0
            #faky = 0  # faktoren der fariabelnen für x und y
            #fakx = 0


            if keys[pygame.K_UP] and barrelrotation <= 240:
                barrelrotation = barrelrotation + 5
                bullet_grad_plus()

            if keys[pygame.K_DOWN] and barrelrotation >= 180:
                barrelrotation = barrelrotation - 5
                bullet_grad_minus()

            win.blit(blaueshartesding, (p.x + 85- int(blaueshartesding.get_width() / 2), p.y + 75  - int(blaueshartesding.get_height() / 2)))

            win.blit(rotes_hartes_ding_turned, (p2.x + 15, p2.y + 75 ))
            #print(barrelrotation)
#hier shooting mech p1
            if keys[pygame.K_w]:  #flugdauer + bzw vershiebt den hochpunkt
                bullet_weite()
                #print('Staerke: '+ bullet_staerke)

            if keys[pygame.K_s]: #flugdauer -
                bullet_kurz()
                #print('Staerke: '+ bullet_staerke)

            if keys[pygame.K_q]:
                bullet_grad_plus()
                #print('Winkel: '+ bullet_winkel)

            if keys[pygame.K_a]:
                bullet_grad_minus()
                #print('Winkel: '+bullet_winkel)
            if keys[pygame.K_r]:
                reset_bullet_trajectory()
                barrelrotation = 230



            if keys[pygame.K_SPACE]:
               # print('Hello i am under the water')


                fire_bullet(p.x , p.y )
                distanz = 0
#hhhhurfrujfu

            if bullet_state is True:

                 bulletx = p.x
                 bullety = p.y
                 bullet_shoot = True

                 while bullet_shoot:      #while variX < 900 V1.0 schuss geht gerade aus
                     #hier for loop
                     #distanz =0

                     for x in range(bullet_staerke * 2) :

                        variX = variX + (fakx)

                        distanz = distanz + 2

                     # if  else für ab hälfte das andere
                        if distanz < (bullet_staerke  ):
                            variY = variY - (faky)
                            fire_bullet(bulletx + variX, bullety + variY)
                        elif distanz > (bullet_staerke  ):# and distanz != (bullet_staerke*4)
                            variY = variY + (faky) #war mal 5
                            fire_bullet(bulletx + variX, bullety + variY)
                        elif distanz == bullet_staerke:

                            bullet_shoot = False
                            stop_bullet()
                            break





                     fire_bullet(bulletx + variX, bullety + variY)
                     if variX > 400:
                         bullet_shoot = False
                         stop_bullet()













            """ bullet_group.add(Bullegame.create_bullet(p.x, p.y)) """



        if p.id == "Player 2":

            roteshartesding = pygame.transform.rotate(rotes_hartes_ding, barrelrotation)
            keys = pygame.key.get_pressed()
            barrelrotation = 230

            variX = 0  # wie stark das zeug ist bzw winkel
            variY = 0
            # faky = 0  # faktoren der fariabelnen für x und y
            # fakx = 0
            win.blit(roteshartesding, (p.x +35 - int(roteshartesding.get_width() / 2), p.y + 90 + 116 - int(roteshartesding.get_height() / 2)))
            win.blit(blaueshartesding,(p2.x+ 20 , p2.y +120))

            if keys[pygame.K_UP] and barrelrotation > 120:
                barrelrotation = barrelrotation - 5

            if keys[pygame.K_DOWN] and barrelrotation <= 180:
                barrelrotation = barrelrotation + 5

            win.blit(blaueshartesding,(p2.x+ 20 , p2.y +120))
            win.blit(roteshartesding, (p.x +35 - int(roteshartesding.get_width() / 2), p.y + 90 + 116 - int(roteshartesding.get_height() / 2)))
            #print(barrelrotation)

            if keys[pygame.K_w]:  #flugdauer + bzw vershiebt den hochpunkt
                bullet_weiteP2()
                #print('Staerke: '+ bullet_staerke)

            if keys[pygame.K_s]: #flugdauer -
                bullet_kurz()
                #print('Staerke: '+ bullet_staerke)

            if keys[pygame.K_q]:
                bullet_grad_plus()
                #print('Winkel: '+ bullet_winkel)

            if keys[pygame.K_a]:
                bullet_grad_minus()
                #print('Winkel: '+bullet_winkel)
            if keys[pygame.K_r]:
                reset_bullet_trajectory()
                barrelrotation = 230



            if keys[pygame.K_SPACE]:
               # print('Hello i am under the water')


                fire_bullet(p2.x , p2.y )
                distanz = 0


            if bullet_state is True:

                 bulletx = p2.x
                 bullety = p2.y
                 bullet_shoot = True

                 while bullet_shoot:      #while variX < 900 V1.0 schuss geht gerade aus
                     #hier for loop
                     #distanz =0

                     for x in range(bullet_staerke * 2) :

                        variX = variX - (fakx)

                        distanz = distanz + 2

                     # if  else für ab hälfte das andere
                        if distanz < (bullet_staerke  ):
                            variY = variY - (faky)
                            fire_bullet(bulletx + variX, bullety + variY)
                        elif distanz > (bullet_staerke  ):# and distanz != (bullet_staerke*4)
                            variY = variY + (faky) #war mal 5
                            fire_bullet(bulletx + variX, bullety + variY)
                        elif distanz == bullet_staerke:

                            bullet_shoot = False
                            stop_bullet()
                            break





                     fire_bullet(bulletx + variX, bullety + variY)
                     if variX > 400:
                         bullet_shoot = False
                         stop_bullet()








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