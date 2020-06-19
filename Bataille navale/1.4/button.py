import pygame


class Button:
    def __init__(self, x_max, x_min, y_max, y_min, surface, color):
        self.triggered = False
        self.color = color
        self.mouse_state = pygame.mouse.get_pressed()
        self.mouse = pygame.mouse.get_pos()
        self.width = x_max - x_min
        self.height = y_max - y_min
        print(self.mouse[0])
        if x_min < self.mouse[0] < x_max and y_min < self.mouse[1] < y_max and self.mouse_state[0]:
            self.triggered = True
            self.color = (0, 255, 0)
            self.x = self.mouse[0]
            self.y = self.mouse[1]
        pygame.draw.rect(surface, self.color, (x_min, y_min, self.width, self.height))


