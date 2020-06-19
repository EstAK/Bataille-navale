import pygame
import random

# faction 0 = DE
# faction 1 = JP
# faction 2 = IT
# faction 3 = US
# faction 4 = FR
# faction 5 = UK
# carré = 42p*44p


class Selection:
    def __init__(self, display):
        self.image = pygame.image.load('grille_pain.jpg')
        display.blit(self.image, (0, 0))










