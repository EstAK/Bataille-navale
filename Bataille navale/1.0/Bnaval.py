import pygame
pygame.init()

screen_width = 1024
screen_height = 576
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(' Bataille navale')

background_color = (0, 0, 0)
screen.fill(background_color)
pygame.display.update()
background = pygame.image.load('grille_pain.png')
running = True
x = 0
y = 0


def grille(x, y):
    screen.blit(background, (x, y))


while running:
    pygame.time.delay(75)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.time.delay(50)
            running = False
    keys = pygame.key.get_pressed()