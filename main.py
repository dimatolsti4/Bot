import sys
import pygame
from character import *
from chtoto import *
from pygame.locals import *

WINDOW_SIZE = (600, 400)
FPS = 60

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
# display = pygame.Surface(WINDOW_SIZE)

blocks = create_map(WINDOW_SIZE)

clock = pygame.time.Clock()

finished = False

while not finished:
    # try:
    screen.fill(255)
    clock.tick(FPS)



    """except BaseException as e:
        print(str(e))
        break"""

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
            for block in blocks:
                if block.x + block.size > event.pos[0] > block.x and \
                        block.y + block.size > event.pos[1] > block.y and length(event.pos, Character.x, Character.y,
                                                                                 block.size):
                    block.damage()
                    if block.hp <= 0:
                        block.kill(blocks)
                        fall(blocks, screen)
    if Character.moving_right or Character.moving_left or Character.jump:
        if Character.moving_left:
            were_to_go('left', blocks, screen)
        if Character.moving_right:
            were_to_go('right', blocks, screen)
        if Character.jump:
            up_jump(blocks, screen)
            print (Character.jump)
        fall(blocks, screen)
        draw_p(screen)
    else:
        draw_p(screen)

    for block in blocks:
        block.draw(screen)
    pygame.display.update()
pygame.display.quit()
pygame.quit()
