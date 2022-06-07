import pygame


class Player():
    def __init__(self, x, y, height, width,color):
        self.x = x
        self.y = y
        self.height =height
        self.color =color
        self.width = width
        self.tank = (x,y,width,height)
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

