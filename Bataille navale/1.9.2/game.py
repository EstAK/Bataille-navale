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
        i = 0       # varible compteur
        count = 0       # variable compteur
        iscomplete = False      # état du posage des bateaux
        client_ship = []        # coordonnées des bateaux confondues
        ship_list = [('PA.png', 5), ('CR.png', 4), ('SM.png', 3), ('SM.png', 3), ('TP.png', 2)]     # liste des bateaux et longueurs
        coord_list = []     # tuple temporaire

        running = True      # mise en place de la boucle principale
        while running:
            pygame.time.delay(1)       # délai d'action en milli secondes
            for event in pygame.event.get():        # détecteur d'évènement
                if event.type == pygame.QUIT:       # condition pour quitter sans crasher le jeux
                    running = False     # ligne permettant de quitter sans crasher la fenêtre

            keys = pygame.key.get_pressed()     # détection des touches

            Selection(screen)       # apparition de l'arrière plan

            angle = 0       # première définition de l'angle du bateau

            if not pygame.mouse.get_pressed()[0]:       # condition pour poser un bateau ( clic gauche )
                mouse = pygame.mouse.get_pos()      # attribution des coordonnées x,y de la souris à la variable mouse
                x, y = mouse[0], mouse[1]       # distribution des valeurs de la variable mouse à x, y
            else:
                pos_x, pos_y = int((x - 50) / 42), int((y - 53) / 44)       # calcul de la case sur laquelle le bateau se trouve
                x, y = pos_x*42 + 50, pos_y*44 + 53     # "clippage" de l'image sur le quadrilage

                if keys[pygame.K_KP_ENTER]:     # condition pour récuperer toutes les coordonnées d'un bateau ( ENTER sur le pavé numérique )
                    if pygame.mouse.get_pos()[1] > y:       # condition pour calculer les coordonnés si l'on veut placer le bateau verticalement
                        for o in range((ship_list[i])[1]):      # longueur du bateau en question prise 1:1
                            coord_temp = (pos_x, pos_y + o)     # variable temporaire
                            coord_list.append(coord_temp)       # ajout de la variable temporaire à la tuple temporaire

                        for p in coord_list:        # détecteur de répétition avec les coordonnés du client
                            for q in client_ship:
                                if p == q:      # condition d'égalité entre toutes coordonnés client et coordonnées entrée
                                    coord_list.clear()      # si chevauchment de coordonnée alors effacer la coordonéé temporaire

                        if len(coord_list) > 0:     # si la coordonnée temporaire est différente en tout point de celles du client
                            client_ship = client_ship + coord_list      # somme des coordonnées client et celles temporaires
                            del ship_list[i]        # supression du bateau déjà placé de la liste des bateaux en attente
                            count += 1      # compteur
                            coord_list.clear()      # suppresion de la tuple temporaire

                        pygame.time.wait(125)       # délai pour le comfort

                    else:
                        for o in range((ship_list[i])[1]):      # même condition qu'à la ligne 53 mais, pour les bateaux horizontaux
                            coord_temp = (pos_x + o, pos_y)
                            coord_list.append(coord_temp)

                        for p in coord_list:
                            for q in client_ship:
                                if p == q:
                                    coord_list.clear()

                        if len(coord_list) > 0:
                            client_ship = client_ship + coord_list
                            del ship_list[i]
                            count += 1
                            coord_list.clear()

                            pygame.time.wait(125)

                    pygame.time.wait(125)

                if pygame.mouse.get_pos()[1] > y:       # rotation verticale visuelle du bateau
                    angle = 90

            if keys[pygame.K_SPACE]:        # condition pour changer de bateau
                pygame.time.wait(125)       # délai pour éviter un défilement trop rapide
                i += 1      # variable compteur de l'emplacement dans la tuple
            if i > len(ship_list)-1:        # condition pour revenir au premier revenir au premier bateau du tuple
                i = 0

            if count == 5:      # condition pour savoir quand tout les bateaux sont placés
                iscomplete = True

            print(i)
            ship = Button(screen)  # initialisation des bateaux
            if not iscomplete:      # tant que tout les bateaux ne sont pas placés
                ship.rect_draw((ship_list[i])[0], (x, y), angle)     # apparition de bateau avec hit box

            pygame.display.update()  # mise à jour de la fenêtre





















