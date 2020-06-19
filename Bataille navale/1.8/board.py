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

    def __init__(self, display, coord_min, orientation):
        self.coord = coord_min
        self.orientation = orientation
        self.image = pygame.image.load('grille_pain.jpg')
        display.blit(self.image, (0, 0))

    def ship(self, size):
        # orientation : [Top],[Right],[Down],[Left]
        if self.orientation == 'Top':
            self.coord[1] += size
        if self.orientation == 'Right':
            self.coord[0] += size
        if self.orientation == 'Down':
            self.coord[1] -= size
        if self.orientation == 'Left':
            self.coord[0] -= size
        return self.coord









