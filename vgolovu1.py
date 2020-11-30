import pygame, sys, os, random
clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('Platformer')

WINDOW_SIZE = (600,400)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

display = pygame.Surface((300,200))

moving_right = False
moving_left = False
air_timer = 0

CHUNK_SIZE = 8

global animation_frames
animation_frames = {}

blocks = []

player_rect = pygame.Rect(100,100,5,13)

player_surface = pygame.Surface((player_rect.w, player_rect.h))

player_digging = False

BLOCK_DURATION = 5
block_stage = BLOCK_DURATION
block = pygame.Rect(120,120,50,50)
block_surface = pygame.Surface((block.h, block.w))

def move(*args):
    ""

while True:

    screen.fill(255)

    screen.blit(player_surface, (100, 100))
    screen.blit(block_surface, (120, 120))


    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                ""
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            if 120 + block.w > event.pos[0] > 120 and 120 + block.h > event.pos[0] > 120:
                block_stage -= 1
                if block_stage <= 0:
                    block_surface = pygame.Surface((0,0))
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0)
else:
    pygame.display.set_mode(0)
    pygame.quit()
    exit(0)
'sasad'
