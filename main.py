import pygame, sys


def draw_floor():
    screen.blit(floor_surface, (floor_x, 785))
    screen.blit(floor_surface, (floor_x + -576, 785))


pygame.init()
screen = pygame.display.set_mode((576, 900))
clock = pygame.time.Clock()

# Game Variables
grav = 0.25
bird_movement = 0

background_surface = pygame.transform.scale2x(pygame.image.load('images/background-day.png')).convert()
# background_surface = pygame.transform.scale2x(background_surface)

floor_surface = pygame.transform.scale2x(pygame.image.load('images/base.png'))

# floor_surface = pygame.image.load('images/base.png').convert()

floor_x = 0

bird_surface = pygame.transform.scale2x(pygame.image.load('images/bluebird-midflap.png').convert())
bird_hb = bird_surface.get_rect(center=(425, 450))

while True:

    # image of player 1
    # background image

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 12
                # print("any flappers in chat")

    pygame.display.update()
    clock.tick(144)

    screen.blit(background_surface, (0, 0))

    bird_movement += grav
    bird_hb.centery += bird_movement

    screen.blit(bird_surface, bird_hb)
    floor_x += 1
    draw_floor()
    if floor_x >= 576:
        floor_x = 0
