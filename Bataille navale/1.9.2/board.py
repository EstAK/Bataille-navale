import pygame
import random

# faction 0 = DE
# faction 1 = JP
# faction 2 = IT
# faction 3 = US
# faction 4 = FR
# faction 5 = UK
# carré = 41p*43p


class Selection:
    def __init__(self, display):
        self.display = display
        self.image = pygame.image.load('grille_pain.jpg')
        self.display.blit(self.image, (0, 0))
        self.color = (245, 20, 230)











