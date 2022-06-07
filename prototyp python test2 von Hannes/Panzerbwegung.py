import pygame


class Player():
    def __init__(self, x, y, tank):
        self.x = x
        self.y = y
        self.tank = pygame.image.load("Blue-Tank-V1.png")
        self.vel = 5
       # self.turr = pygame.image.load("Blue-tank-Kanone-v1-nutzen")
        #self.vel2 = 0.5

    def tank_move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        self.update()

    #def turret_move(self):
    #    keys = pygame.key.get_pressed()

    #    if keys[pygame.K_UP]:
    #        self.y += self.vel2

     #   if keys[pygame.K_DOWN]:
      #      self.y -= self.vel2

      #  self.update()

    def update(self):
        self.tank = self.x
        #self.turr = self.y

