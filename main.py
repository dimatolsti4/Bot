import pygame

from pygame.locals import *
pygame.init()

WINDOW_SIZE = (600,400)
FPS = 60

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

display = pygame.Surface((300,200))

blocks = create_map()
player = character()

clock = pygame.time.Clock()
finished = False

while not finished:
    screen.fill(255)
    clock.tick(FPS)

    player.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                pass
            if event.key == K_LEFT:
                pass
            if event.key == K_UP:
                pass
            
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                pass
            if event.key == K_LEFT:
                pass
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            for block in blocks:
                if block.x + block.size_x > event.pos[0] > block.x and \
                   block.y + block.size_y > event.pos[1] > block.size_y:
                    block.damage()
                    if block.hp <= 0:
                        block.kill()




    for block in blocks:
        block.draw()
    pygame.display.update()    
    time += 1
pygame.quit()
