import pygame
import sys
import random


def draw_floor():
    screen.blit(floor_surface, (floor_x, 785))
    screen.blit(floor_surface, (floor_x + -576, 785))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(-700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(-700, random_pipe_pos - 350))
    return bottom_pipe, top_pipe


def moving_pipes(pipes):
    for pipe in pipes:
        pipe.centerx += 5
    return pipes


def drawing_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:

            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


def check_coll(pipes):
    for pipe in pipes:
        if bird_hb.colliderect(pipe):
            # print('collision')
            return False

    if bird_hb.top <= -100 or bird_hb.bottom >= 785:
        # print("out of screen")
        return False

    return True


def rotate_bird(bird):
    rotating_bird = pygame.transform.rotozoom(bird, bird_movement * 50, 1)
    return rotating_bird


def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 100))
        screen.blit(score_surface, score_rect)

    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score: {int(score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(288, 550))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


pygame.init()

pygame.display.set_caption("crappy birb")
screen = pygame.display.set_mode((576, 900))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19__.TTF', 40)

# Game Variables
grav = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0

# icon

ICON = pygame.transform.scale2x(pygame.image.load('images/icon.png')).convert()
pygame.display.set_icon(ICON)

background_surface = pygame.transform.scale2x(pygame.image.load('images/background-day.png')).convert()
# background_surface = pygame.transform.scale2x(background_surface)

floor_surface = pygame.transform.scale2x(pygame.image.load('images/base.png'))

# floor_surface = pygame.image.load('images/base.png').convert()

floor_x = 0

bird_surface = pygame.transform.scale2x(pygame.image.load('images/bluebird-midflap.png').convert_alpha())
bird_hb = bird_surface.get_rect(center=(425, 450))

pipe_surface = pygame.transform.scale2x(pygame.image.load('images/pipe-green.png'))
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [450, 500, 550, 600, 650, 700, 750]

while True:

    # image of player 1
    # background image

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:  # i wanna make this left click as well
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 12

            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_hb.center = (425, 450)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

            # print("any flappers in chat")

    pygame.display.update()
    clock.tick(144)

    screen.blit(background_surface, (0, 0))

    if game_active:
        # Bird

        bird_movement += grav
        rotated_bird = rotate_bird(bird_surface)
        bird_hb.centery += bird_movement
        screen.blit(rotated_bird, bird_hb)
        game_active = check_coll(pipe_list)

        # Pipes
        pipe_list = moving_pipes(pipe_list)
        drawing_pipes(pipe_list)

        score += 0.01
        score_display('main_game')
    else:
        high_score = update_score(score, high_score)
        score_display('game_over')

        # Floor

    floor_x += 1
    draw_floor()
    if floor_x >= 576:
        floor_x = 0
