import pygame


#ddd

class Player():   #alles hier wird an den server gesendet
    def __init__(self, x, y, height, width, color, id, health, hp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.id = id
        self.rect = (x, y, width, height)
        self.vel = 5
        self.vel2 = 0.5
        self.health = health
        self.hp = hp

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)


    def tank_move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        self.update()

    def turret_move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y += self.vel2

        if keys[pygame.K_DOWN]:
            self.y -= self.vel2

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
        self.turr = self.y







# bullet_gruppe =pygame.sprite.Group() muss noch irgendwo rein gemacht werden


