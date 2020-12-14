import sys
import pygame
from character import *
from blocks import *
from pygame.locals import *

BACKGROUND_COLOR = (0, 170, 170)

WINDOW_SIZE = (600, 400)
FPS = 60
phase_1 = 0
phase_2 = 0
start_damage = 0
pos = 0
proximity_check = False

SCORE = 0

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
font = pygame.font.SysFont('Consolas', 30)

blocks = create_map(WINDOW_SIZE)

clock = pygame.time.Clock()

finished = False

while not finished:
    screen.fill(BACKGROUND_COLOR)
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                Character.moving_right = True
                Character.orientation = True
            if event.key == pygame.K_a:
                Character.moving_left = True
                Character.orientation = False
            if event.key == pygame.K_SPACE and Character.jump == False:
                Character.jump = True
                were_to_go('jump', blocks, screen)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                Character.moving_right = False
            if event.key == pygame.K_a:
                Character.moving_left = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            xy = nearest_block(Character.x, screen.get_height() // 2, blocks, screen)
            for block in blocks:
                if block.x + block.size > event.pos[0] > block.x \
                        and block.y + block.size > Character.y + event.pos[1] - screen.get_height() // 2 > block.y \
                        and length(event.pos, xy[0], xy[1], block.size, blocks, screen):
                    block.damage()
                    block.use = 1
                    start_damage = 1
                    phase_2 = 1
                    pos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            start_damage = 0
            phase_2 = 0
            for block in blocks:
                if block.use == 1:
                    block.use = 0
    xy = nearest_block(Character.x, screen.get_height() // 2, blocks, screen)
    for block in blocks:
        if block.use == 1 and start_damage == 1 \
                and block.x + block.size > pos[0] > block.x \
                and block.y + block.size > Character.y + pos[1] - screen.get_height() // 2 > block.y \
                and length(pos, xy[0], xy[1], block.size, blocks, screen):
            print("fuck")
            block.damage()
            proximity_check = True
        if block.hp <= 0:
            SCORE = block.kill(blocks, SCORE)
            fall(blocks, screen)
            phase_2 = 0
            block.use = 0
            start_damage = 0
    if proximity_check:
        phase_2 = 1
    else:
        phase_2 = 0
    if Character.moving_right or Character.moving_left or Character.jump:
        if Character.moving_left:
            were_to_go('left', blocks, screen)
        if Character.moving_right:
            were_to_go('right', blocks, screen)
        if Character.jump:
            up_jump(blocks, screen)
        fall(blocks, screen)
        phase_1 += 1
        if Character.jump:
            draw_p(screen, 3)
        else:
            draw(screen, phase_1, phase_2)
    else:
        if phase_2 == 1:
            phase_1 += 1
            draw(screen, phase_1, phase_2)
        else:
            draw_p(screen, 0)

    for block in blocks:
        block.draw(screen, Character.y)
    screen.blit(font.render(('Score:' + str(SCORE)), True, (0, 0, 0)), (32, 48))
    pygame.display.update()
    proximity_check = False

pygame.display.quit()
pygame.quit()
