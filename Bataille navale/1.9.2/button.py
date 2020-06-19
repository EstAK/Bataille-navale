import pygame


class Button:
    def __init__(self, surface):
        self.color = (245, 20, 230)
        self.surface = surface

    def rect_draw(self, ship, coord, angle):
        image = pygame.image.load(ship)
        image.convert()
        image = pygame.transform.rotozoom(image, angle, 1)
        objct = image.get_rect()
        self.surface.blit(image, (coord[0], coord[1]))
        pygame.Rect.move_ip(objct, coord[0], coord[1])
        pygame.draw.rect(self.surface, self.color, objct, 1)














