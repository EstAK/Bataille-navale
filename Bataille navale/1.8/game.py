import pygame
import random

from board import Selection
from button import Button


class Game:

    def __init__(self, width, height):
        self.width = width      # largeur de la fenêtre
        self.height = height        # hauteur de la fenêtre

        pygame.init()       # lancement de pygame
        screen = pygame.display.set_mode((self.width, self.height))     # début de la fenêtre
        pygame.display.set_caption(' Bataille navale')      # nommage de la fenêtre
        background_color = (245, 20, 230)       # couleur de l'arrière plan rose pour repèrer artéfact graphique
        screen.fill(background_color)       # remplissage de l'arrière plan avec la couleur sélectionnée
        pygame.display.update()     # mise à jour de la fenêtre
        ships = [('PA', 5), ('C', 4), ('SM', 3), ('SM', 3), ('T', 1)]

        running = True      # mise en place de la boucle principale
        while running:
            pygame.time.delay(0)       # délai d'action en milli secondes
            for event in pygame.event.get():        # détecteur d'évènement
                if event.type == pygame.QUIT:       # condition pour quitter sans crasher le jeux
                    running = False
            Selection(screen, (1, 1), 'Top')
            Button(background_color, 42, 44)
            pygame.display.update()  # mise à jour de la fenêtre












