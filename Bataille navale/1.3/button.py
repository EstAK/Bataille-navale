import pygame


class Button:
    def __init__(self, x_max, x_min, y_max, y_min):
        self.x_max = x_max
        self.x_min = x_min
        self.y_max = y_max
        self.y_min = y_min
        self.triggered = False
        self.mouse = pygame.mouse.get_pressed()
        if x_min < self.mouse[0] < x_max and y_min < self.mouse[1] < y_max:
            self.triggered = True

    def picture_swap(self, first_picture, second_picture):
        self.image = pygame.image.load(first_picture)
        if self.triggered:
            self.image = pypygame.image.load(second_picture)

    def drawing(self, surface, color):
        pygame.draw.rect(surface, color, (self.x_min, self.y_min, self.x_max-self.x_min, self.y_max-self.y_min))