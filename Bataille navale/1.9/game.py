import pygame

from board import Selection
from button import Button


class Game:

    def __init__(self, width, height):
        self.width = width      # largeur de la fenêtre
        self.height = height        # hauteur de la fenêtre

        pygame.init()       # lancement de pygame
        screen = pygame.display.set_mode((self.width, self.height))     # début de la fenêtre arière
        pygame.display.set_caption(' Bataille navale')      # nommage de la fenêtre
        background_color = (245, 20, 230)       # couleur de l'arrière plan rose pour repèrer artéfact graphique
        screen.fill(background_color)       # remplissage de l'arrière plan avec la couleur sélectionnée
        pygame.display.update()     # mise à jour de la fenêtre
        ship_list = ['DE_PA.png']
        i = 0

        running = True      # mise en place de la boucle principale
        while running:
            pygame.time.delay(0)       # délai d'action en milli secondes
            for event in pygame.event.get():        # détecteur d'évènement
                if event.type == pygame.QUIT:       # condition pour quitter sans crasher le jeux
                    running = False     # ligne permettan de quitter sans crasher la fenêtre
            Selection(screen)       # apparition de l'arrière plan
            ship = Button(screen)       # initialisation des bateaux
            #if ship.trigger:
                #i += 1
            ship.rect_draw(ship_list[i])     # apparition de bateau avec hit box
            pygame.display.update()  # mise à jour de la fenêtre












