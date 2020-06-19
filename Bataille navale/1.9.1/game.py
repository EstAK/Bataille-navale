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
        i = 0
        isplacing = False

        running = True      # mise en place de la boucle principale
        while running:
            pygame.time.delay(1)       # délai d'action en milli secondes
            for event in pygame.event.get():        # détecteur d'évènement
                if event.type == pygame.QUIT:       # condition pour quitter sans crasher le jeux
                    running = False     # ligne permettan de quitter sans crasher la fenêtre

            ship_list = ['DE_PA.png', 'UK_PA.png', 'URRS_PA.png', 'US_PA.png']
            keys = pygame.key.get_pressed()
            Selection(screen)       # apparition de l'arrière plan
            if keys[pygame.K_SPACE]:
                pygame.time.wait(125)
                i += 1
            if i > len(ship_list)-1:
                i = 0

            if not pygame.mouse.get_pressed()[0]:
                mouse = pygame.mouse.get_pos()
            else:
                isplacing = True
            x, y = mouse[0], mouse[1]
            ship = Button(screen)  # initialisation des bateaux
            print(ship.rect_draw(ship_list[i], (x,y)))     # apparition de bateau avec hit box


            pygame.display.update()  # mise à jour de la fenêtre












