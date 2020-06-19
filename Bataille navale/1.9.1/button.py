import pygame


class Button:
    def __init__(self, surface):
        self.color = (245, 20, 230)
        self.trigger = pygame.mouse.get_pressed()[0]
        self.surface = surface

    def rect_draw(self, ship, coord):
        image = pygame.image.load(ship)
        image.convert()
        objct = image.get_rect()
        self.surface.blit(image, (coord[0], coord[1]))
        pygame.Rect.move_ip(objct, coord[0], coord[1])
        pygame.draw.rect(self.surface, self.color, objct, 1)
        if self.trigger:
            pos_x, pos_y = int((coord[0] - 50)/42), int((coord[1] - 53)/44)
            return pos_x, pos_y













