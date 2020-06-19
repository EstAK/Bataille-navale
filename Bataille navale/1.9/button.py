import pygame


class Button:
    def __init__(self, surface):
        self.color = (245, 20, 230)
        self.mouse = pygame.mouse.get_pos()
        self.trigger = pygame.mouse.get_pressed()[0]
        print(self.mouse[0])
        self.x, self.y = self.mouse[0], self.mouse[1]
        self.surface = surface

    def rect_draw(self, ship):
        angle = 0
        image = pygame.image.load(ship)
        image.convert()
        if self.trigger:
            angle += 90
            image = pygame.transform.rotozoom(image, angle, 1)
        objct = image.get_rect()
        self.surface.blit(image, (self.x, self.y))
        pygame.Rect.move_ip(objct, self.x, self.y)
        pygame.draw.rect(self.surface, self.color, objct, 1)














