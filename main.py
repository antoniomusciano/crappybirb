import pygame, sys


def draw_floor():
    screen.blit(floor_surface, (floor_x, 900))
    screen.blit(floor_surface, (floor_x + -576, 900))


pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()

background_surface = pygame.transform.scale2x(pygame.image.load('images/background-day.png')).convert()
# background_surface = pygame.transform.scale2x(background_surface)

floor_surface = pygame.transform.scale2x(pygame.image.load('images/base.png'))

# floor_surface = pygame.image.load('images/base.png').convert()

floor_x = 0

while True:

    # image of player 1
    # background image

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(144)

    screen.blit(background_surface, (0, 0))
    floor_x += 1
    draw_floor()
    if floor_x >= 576:
        floor_x = 0
