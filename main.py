import pygame
from character import *
from pygame.locals import *
pygame.init()

WINDOW_SIZE = (600,400)
FPS = 60

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

display = pygame.Surface(WINDOW_SIZE)

blocks = create_map()
player = character()

clock = pygame.time.Clock()
finished = False
moving_right = False
moving_left = False
jump = False

while not finished:
    screen.fill(255)
    clock.tick(FPS)

    player.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_SPACE:
                jump = True
                were_to_go('jump', blocks, screen)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_a:
                moving_left = False
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            for block in blocks:
                if block.x + block.size_x > event.pos[0] > block.x and \
                   block.y + block.size_y > event.pos[1] > block.size_y:
                    block.damage()
                    if block.hp <= 0:
                        block.kill()
    if moving_right or moving_left or jump:
        if moving_left:
            were_to_go('left', blocks, screen)
        if moving_right:
            were_to_go('right', blocks, screen)
        if jump:
            up_jump(blocks, screen, jump)
        draw(0, screen)
    else:
        draw(1, screen)




    for block in blocks:
        block.draw()
    pygame.display.update()    
pygame.quit()
