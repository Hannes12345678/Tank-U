import pygame
from tank_Network import Network
from Panzerbwegung import *
import pygame
import Knopfklasse
import pygame.math
#from math import pi
#from math import cos
#from math import sin

n = Network() #networking geschichte
p = n.getP() #player relevante dinge
t = n.getP()
p2 = n.send(p)
#bullet variablen (können später gemacht werden )
#bullety = p.y
#bulletx = p.x

# alle variablen mit bullet_... stehen im zusammen hang mit der Flugbahn berechnung
bullet_staerke = 15 # hier immer ungerade / für hochpunkt berechnung (FLUGBAHN = DREIECK)
bullet_winkel = 0 # davor 10 / Winkel Einstellung

faky = 5  # faktoren der fariabelnen für x und
fakx = 5
bullet_state = False # Bulletlogic variable
bullet_shoot = False # -/-/-


"""
Das hier war mal für die Flugbahn berechnung gedacht, hat jedoch nicht wirklich funktionier also wurde es anders gelösst 
g = [0, -9.8, 0]
v0 = 10
theta = 30 * pi / 180
r = [0,0,0]
v = v0*[cos(theta), sin(theta), 0]
m = 1
pos = m * v
time = 0
dtime = 0.01 #maybe was anderes
"""


#Display Settings
width = 1001
height = 501
win = pygame.display.set_mode((width, height)) #Gui vorraussetzung

#Großteil der Grafiken also Pixelart

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
winner = pygame.image.load('uwin.png')
loser = pygame.image.load('ulose.png')



bullet_group = pygame.sprite.Group()



#display fester erstellen
SCREEN_HEIGHT = height
SCREEN_WIDTH = width
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('TANK-U')
#Start Menü Grafiken
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
    """
    global g
    global v0    hier war die alte logic drin
    global theta
    global r
    global v
    global m
    global pos
    global time
    global dtime
    """

    bullet_state = True
   # while y < 501 :
    win.blit(runde_kugel,(x+90  , y+55) )  # der ball den man sieht auf dem Bildschirm

def stop_bullet(): #stopt durch False
    global bullet_state
    bullet_state = False
    #print("aufhören")

def bullet_weite(): #hochpunkt einstellung +
    global bullet_staerke
    bullet_staerke = bullet_staerke + 2

    sxs = 250
    if bullet_staerke > sxs:
        bullet_staerke = bullet_staerke - 2
def bullet_kurz(): # hochpunkt einstellung -
    global bullet_staerke
    bullet_staerke = bullet_staerke - 2

    if bullet_staerke < 5:
        bullet_staerke = bullet_staerke + 2

def bullet_grad_plus(): #winkel einstellunng
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
#hhh
def bullet_grad_minus(): # winkel verkleinern
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



def reset_bullet_trajectory(): # wegen leicht buggie winkel einstellung gibt es einen "reset button"
    global fakx
    global faky
    global bullet_winkel
    fakx = 5
    faky = 5
    bullet_winkel =0     # alles wird hier auf den anfangs punkt gesetzt

#def treffer():
def health_registration(a ):     # schadens Logic
    global p2
    global p

    if a <= 0:
        print("win")
        p.x = p.x +10000
        #print p.x muss noch unten rein








#window anzeige

def redrawWindow(win, player, player2): #was auf dem screen sichtbar ist
    pygame.font.init()

    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    win.fill((255, 255, 255))
    win.blit(hinter_grundussus,(0,0))  #hintergrund und ebene
    text_surface = my_font.render('[<- = move left/ move right = -> ; Space = Shoot] ', False, (0, 0, 0))  # steuerungs erklärung
    text_surface2 = my_font.render('[ Arrow up/down = Shooting angle; W/S = shooting Power] ', False, (0, 0, 0))

    screen.blit(text_surface, (10, 450))
    screen.blit(text_surface2, (10,475))
    player.draw(win)
    player2.draw(win)
    bullet_group.draw(win)
    bullet_group.draw(win)


    pygame.display.update()



#Spiel
def main():
    #global winner
    #global loser

    run = True
    winner = pygame.image.load('uwin.png')  #winner screen
    loser = pygame.image.load('ulose.png') #loser screen
    """n = Network()
    p = n.getP()  #ist jetzt oben drinn muss was überprüfen 
    t = n.getP()"""
    clock = pygame.time.Clock()
    p2 = n.send(p)


    health_points = p2.hp
    current_time = 0
    go1 = True #bedingung für runden bassiertes system
    go2 = False
    zeit = 0 #beides variablen für die zeit rechnung un runden basierung
    zeitb = 60
    lose = False #winning variable
    winning = False


    barrelrotation = 230
    while run:
        clock.tick(20)  #20 fps
        p2 = n.send(p)
        zeit = zeit + 1 # timer zähler variable





        """if lose:
            win.blit(loser, (0, 0)) das war der erste ansatz für die winner screens 

        elif winning:
            win.blit(winner, (0, 0))"""


        for event in pygame.event.get(): #quit möglichkeit
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.tank_move()  #movement logic
        if zeit == zeitb:   #runden logic
            go1 = False
            go2 = True # ll
        elif zeit == zeitb * 2:
            go1 = True
            go2 = False #go1 und go2 stehen hier für die zweite variable in der "and" funktion
            zeit = 0


        #print(p)
        #print(p2)
        #print(p.x)
        #print(p.y)     alles hier sind daten zum testen gewesen
        #print(p2.x)
        #print(p2.y)
        redrawWindow(win, p, p2)
        """bullety = p.y
        bulletx = p.x"""


        if p.id == "Player 1":
            win.blit(roter_panzer, (p2.x + 50, p2.y))  #bei beiden Playern werden die ansichten bestimmt also wo sie was wie wo sehen
            win.blit(blauer_panzer, (p.x, p.y))

        if p.id == "Player 2":
            win.blit(roter_panzer, (p.x, p.y ))
            win.blit(blauer_panzer, (p2.x, p2.y))


        if p.id == "Player 1" and go1 : #und ermöglicht runden bassierung Player 1 ist ID vom server
            blaueshartesding = pygame.transform.rotate(blaues_hartes_ding_turned, barrelrotation)
            keys = pygame.key.get_pressed()
            barrelrotation = 230


            variX = 0 #wie stark das zeug ist bzw winkel
            variY = 0
            #faky = 0  # faktoren der fariabelnen für x und y
            #fakx = 0
            if lose:
                win.blit(loser, (0, 0))

            if winning:
                win.blit(winner, (0, 0))   #lassen die screens für winning auf flickern

            print(p2.x)
            if p.x >= 2500: #die position des spielers wird genutzt um den gewinner zu erfassen, ist eine einfache art dies zu tun
                print('Super win')
                winning = True

            if p2.x >= 2500 or (p.x + 1800) < p2.x:   # -/-/-
                print('you lose')
                lose = True



            if keys[pygame.K_UP] and barrelrotation <= 240: # rotation des Kanonen laufs und schieß winkel
                barrelrotation = barrelrotation + 5
                bullet_grad_plus()

            if keys[pygame.K_DOWN] and barrelrotation >= 180: # rotation des Kanonen laufs und schieß winkel
                barrelrotation = barrelrotation - 5
                bullet_grad_minus()

            win.blit(blaueshartesding, (p.x + 85- int(blaueshartesding.get_width() / 2), p.y + 75  - int(blaueshartesding.get_height() / 2)))

            win.blit(rotes_hartes_ding_turned, (p2.x + 65, p2.y + 75 ))
            #print(barrelrotation)
#hier shooting mech p1
            if keys[pygame.K_w]:  #flugdauer + bzw vershiebt den hochpunkt
                bullet_weite()
                #print('Staerke: '+ bullet_staerke)

            if keys[pygame.K_s]: #flugdauer -
                bullet_kurz()
                #print('Staerke: '+ bullet_staerke)

            if keys[pygame.K_q]:     # erste winkel einstellung wurde jetzt mit pfeil verknüpft +
                bullet_grad_plus()
                #print('Winkel: '+ bullet_winkel)

            if keys[pygame.K_a]:  # erste winkel einstellung wurde jetzt mit pfeil verknüpft -
                bullet_grad_minus()
                #print('Winkel: '+bullet_winkel)
            if keys[pygame.K_r]:   #reset knopf
                reset_bullet_trajectory()
                barrelrotation = 230
            #if statement für px (muss noch bei p2 rein)


            if keys[pygame.K_SPACE]: #schießen
               # print('Hello i am under the water')


                fire_bullet(p.x , p.y )
                distanz = 0
#schießlogic beginnt hier

            if bullet_state is True:

                 bulletx = p.x # nimmt position vom spieler
                 bullety = p.y
                 bullet_shoot = True


                 while bullet_shoot:      #while variX < 900 V1.0 schuss geht gerade aus
                     #hier for loop
                     #distanz =0

                     for x in range(bullet_staerke * 2) :

                        variX = variX + (fakx)

                        distanz = distanz + 2

                     # if  else für ab hälfte das andere / logic für dreieck flugbahn
                        if distanz < (bullet_staerke  ):
                            variY = variY - (faky)
                            fire_bullet(bulletx + variX, bullety + variY)
                            if (bulletx + variX - 20) <= (p2.x) and (bulletx + variX + 20) >= (p2.x):  # das ganze ding ist die hitboxlogic

                                if (bullety + variY - 20) <= (p2.y) and (bullety + variY + 20) >= (p2.y): #hitboxlogic
                                    print('hit')
                                    health_points = health_points - 5
                                    print(health_points)
                                    health_registration(health_points) # dies funktion wiederholt sich um alle fälle ab zu decken


                        elif distanz > (bullet_staerke  ):# and distanz != (bullet_staerke*4)
                            variY = variY + (faky) #war mal 5
                            fire_bullet(bulletx + variX, bullety + variY)
                            if (bulletx + variX - 20) <= (p2.x) and (bulletx + variX + 20) >= (p2.x):
                                if (bullety + variY - 20) <= (p2.y) and (bullety + variY + 20) >= (p2.y):
                                    print('hit')
                                    health_points = health_points - 2
                                    print(health_points)
                                    health_registration(health_points)



                        elif distanz == bullet_staerke:

                            bullet_shoot = False
                            stop_bullet()
                            break
                     if (bulletx + variX-20) <= (p2.x) and (bulletx + variX + 20) >= (p2.x):
                        if (bullety + variY-20) <= (p2.y) and (bullety + variY + 20) >= (p2.y):
                            print('hit')
                            health_points = health_points - 2
                            print(health_points)
                            health_registration(health_points)





                     if p.x >= 2500:       #als absicherung
                        print('Super win')
                        winning = True


                     if p2.x >= 2500 or (p.x+1800) < p2.x :

                         print('you lose')

                         lose = True












                     fire_bullet(bulletx + variX, bullety + variY)
                     if variX > 400:
                         bullet_shoot = False
                         stop_bullet()








#heh





            """ bullet_group.add(Bullegame.create_bullet(p.x, p.y)) """
        if p.id == "Player 2" and go2: # die logic aus Player 1 ist hier quasie gleich nur das vorzeichen entsprechen getauscht worden sind
            blaueshartesding = pygame.transform.rotate(rotes_hartes_ding_turned, barrelrotation)
            keys = pygame.key.get_pressed()
            barrelrotation = 300


            variX = 0  # wie stark das zeug ist bzw winkel
            variY = 0
            # faky = 0  # faktoren der fariabelnen für x und y
            # fakx = 0

            if lose:
                win.blit(loser, (0, 0))

            if winning:
                win.blit(winner, (0, 0))

            if p.x >= 2500:
                print('Super win')
                winning = True

            if p2.x >= 2500 or p2.x > p.x:
                print('you lose')
                lose = True

            if keys[pygame.K_UP] and barrelrotation <= 390:
                barrelrotation = barrelrotation - 5
                bullet_grad_plus()

            if keys[pygame.K_DOWN] and barrelrotation >= 280:
                barrelrotation = barrelrotation + 5
                bullet_grad_minus()
#d
            win.blit(blaueshartesding, (
            p.x + 30 - int(blaueshartesding.get_width() / 2), p.y + 75 - int(blaueshartesding.get_height() / 2)))

            win.blit(blaues_hartes_ding, (p2.x + 0, p2.y + 0))
            # print(barrelrotation)
            # hier shooting mech p1
            if keys[pygame.K_w]:  # flugdauer + bzw vershiebt den hochpunkt
                bullet_weite()
                # print('Staerke: '+ bullet_staerke)

            if keys[pygame.K_s]:  # flugdauer -
                bullet_kurz()
                # print('Staerke: '+ bullet_staerke)

            if keys[pygame.K_q]:
                bullet_grad_plus()
                # print('Winkel: '+ bullet_winkel)

            if keys[pygame.K_a]:
                bullet_grad_minus()
                # print('Winkel: '+bullet_winkel)
            if keys[pygame.K_r]:
                reset_bullet_trajectory()
                barrelrotation = 230

            if keys[pygame.K_SPACE]:
                # print('Hello i am under the water')

                fire_bullet(p.x - 50, p.y)
                distanz = 0
            #bullet logic

            if bullet_state is True:

                bulletx = p.x -50
                bullety = p.y
                bullet_shoot = True

                while bullet_shoot:  # while variX < 900 V1.0 schuss geht gerade aus
                    # hier for loop
                    # distanz =0

                    for x in range(bullet_staerke * 2):

                        variX = variX + (fakx)

                        distanz = distanz + 2

                        # if  else für ab hälfte das andere
                        if distanz < (bullet_staerke):
                            variY = variY - (faky)
                            fire_bullet(bulletx - variX, bullety + variY)
                            #print('p2.x : ')
                            #print(p2.x)
                            #print('bulletx - variX + 20 : ')
                            #print(bulletx - variX + 20)
                            #print('bulletx - variX - 20 : ')
                            #print(bulletx - variX - 20)
                            #print('bullety + variY - 20 : ')
                            #print(bullety + variY - 20)
                            #print('bullety + variY + 20 : ')
                            #print(bullety + variY + 20)
                            #print('p2.y : ')
                            #print(p2.y)
                            if (bulletx - variX + 20) >= (p2.x) and (bulletx - variX - 20) <= (p2.x): # muss vllt raus
                                if (bullety + variY - 20) <= (p2.y) and (bullety + variY + 20) >= (p2.y):
                                    #print('hit')
                                    health_points = health_points - 2
                                    print(health_points)
                                    health_registration(health_points)
                        elif distanz > (bullet_staerke):  # and distanz != (bullet_staerke*4)
                            variY = variY + (faky)  # war mal 5
                            fire_bullet(bulletx - variX, bullety + variY)

                            if (bulletx - variX + 20) >= (p2.x) and (bulletx - variX - 20) <= (p2.x):
                                if (bullety + variY - 20) <= (p2.y) and (bullety + variY + 20) >= (p2.y):
                                    #print('hit')
                                    health_points = health_points - 2
                                    print(health_points)
                                    health_registration(health_points)

                        elif distanz == bullet_staerke:

                            bullet_shoot = False
                            stop_bullet()
                            break
                    if (bulletx - variX + 100) >= (p2.x) and (bulletx - variX - 100) <= (p2.x):
                        if (bullety + variY - 100) <= (p2.y) and (bullety + variY + 100) >= (p2.y):
                            #print('hit')
                            health_points = health_points - 2
                            #print(health_points)
                            health_registration(health_points)

                    if p.x >= 2500:
                        print('Super win')
                        winning = True

                    if p2.x >= 2500 or p2.x > p.x:
                        print('you lose')
                        lose = True





                    fire_bullet(bulletx + variX, bullety + variY)
                    if variX > 900:
                        bullet_shoot = False
                        stop_bullet()

            """ bullet_group.add(Bullegame.create_bullet(p.x, p.y)) """

        pygame.display.update()

#main() habe es in kommentar gesetzt damit man bei ui testen kann




run = True
while run: #start

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