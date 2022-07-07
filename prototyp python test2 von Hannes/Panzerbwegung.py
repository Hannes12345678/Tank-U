import pygame


#ddd

class Player():   #alles hier wird an den server gesendet
    def __init__(self, x, y, height, width, color, id, hp, run): # was im spieler drin ist
        self.x = x       #Koordinaten
        self.y = y
        self.width = width #breite
        self.height = height #höhe
        self.color = color #farbe
        self.id = id  #player "nummer"
        self.rect = (x, y, width, height) #Würfel bildung
        self.vel = 5 #geschwindigkeit beim fahren
        self.vel2 = 0.5 # war geadacht für turret wurde aber anders implementiert
        self.hp = hp # lebenspunkte
        self.run = run #variable für funktion

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)


    def tank_move(self):   #panzer bewegung, rechts links
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        self.update()

    def turret_move(self):  # Turret bewegung, wurde anders gelöst
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y += self.vel2

        if keys[pygame.K_DOWN]:
            self.y -= self.vel2

        self.update()

    def update(self):  #update methode zum anzeigen
        self.rect = (self.x, self.y, self.width, self.height)
        self.turr = self.y







# bullet_gruppe =pygame.sprite.Group() muss noch irgendwo rein gemacht werden


