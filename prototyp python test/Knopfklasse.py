import pygame


class knopf():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        #maus position
        pos = pygame.mouse.get_pos()

        # maus über den bildern
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True

                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

# knopf auf dem bildschirm zeigen

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action