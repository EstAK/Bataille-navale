import pygame


class Button:
    def __init__(self, surface, ship, coord, angle):        # fonction d'initialisation servant à distribuer les valeurs parmi les variables
        self.color = (245, 20, 230)
        self.surface = surface
        self.ship = ship
        self.coord = coord
        self.angle = angle

    def rect_draw(self):        # fonction servant à dessiner les images ave un rectangle autour pour les délimiter
        image = pygame.image.load(self.ship)        # chargement de l'image
        image.convert()
        image = pygame.transform.rotozoom(image, self.angle, 1)     # rotation de l'image
        objct = image.get_rect()        # création du rectangle sur base de la résolution de l'image
        self.surface.blit(image, (self.coord[0], self.coord[1]))        # dessin de l'imagee sur une surface donnée
        pygame.Rect.move_ip(objct, self.coord[0], self.coord[1])        # suivi de la souris des coordonnées du rectangle
        pygame.draw.rect(self.surface, self.color, objct, 1)        # dessin du rectangle














