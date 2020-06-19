import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, surface):
        self.color = (245, 20, 230)
        self.mouse = pygame.mouse.get_pos()
        print(self.mouse[0])
        self.x = self.mouse[0]
        self.y = self.mouse[1]

        pygame.draw.rect(surface, self.color, (self.x, self.y, width, height))













