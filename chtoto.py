from pygame.draw import *
import pygame
import numpy as np
from pygame.image import load
from pygame.transform import scale
from character import *

COLOR = {
    'green': (0, 255, 0),
    'yellow': (255, 255, 0)
}
PLAYER_PATH_Static = 'src/Static.png'
PLAYER_PATH_Going = 'src/Going.png'
PLAYER_PATH_Eating = 'src/Eating.png'
PLAYER_PATH_Jumping = 'src/Jumping.png'
PLAYER_SRC_Static = load(PLAYER_PATH_Static)
PLAYER_SRC_Going = load(PLAYER_PATH_Going)
PLAYER_SRC_Eating = load(PLAYER_PATH_Eating)
PLAYER_SRC_Jumping = load(PLAYER_PATH_Jumping)

SCALE = 0.11


class Character:
    x = 200
    y = 50
    vy = 0
    vx = 2
    g = 1
    hp = 10

    orientation = False

    moving_right = False
    moving_left = False
    jump = False

    color = (255, 255, 255)

    player_surface_Static = scale(PLAYER_SRC_Static, (
    int(PLAYER_SRC_Static.get_width() * SCALE), int(PLAYER_SRC_Static.get_height() * SCALE)))
    player_surface_Going = scale(PLAYER_SRC_Going, (
    int(PLAYER_SRC_Going.get_width() * SCALE), int(PLAYER_SRC_Going.get_height() * SCALE)))
    player_surface_Eating = scale(PLAYER_SRC_Eating, (
    int(PLAYER_SRC_Eating.get_width() * SCALE), int(PLAYER_SRC_Eating.get_height() * SCALE)))
    player_surface_Jumping = scale(PLAYER_SRC_Jumping, (
    int(PLAYER_SRC_Jumping.get_width() * SCALE), int(PLAYER_SRC_Jumping.get_height() * SCALE)))

    height_no_jump = player_surface_Static.get_height()
    width_no_jump = player_surface_Static.get_width()
    height_jump = player_surface_Jumping.get_height()


'''def draw(self):
    global display
    pygame.rect(display, self.color, (self.x, self.y, self.x_size, self.y_size))'''


class Block():
    size = 50

    def __init__(self, color, hp, breakable, loot, x, y):
        self.color = color
        self.hp = hp
        self.breakable = breakable
        self.loot = loot  # ochkov

    def create(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def kill(self, blocks):
        blocks.remove(self)

    def damage(self):
        if self.breakable == True:
            self.hp -= 5


def create_map(window_size, offset=2):
    blocks = []
    num_lines = window_size[0] // Block.size
    num_col = window_size[1] // Block.size

    color_green = (0, 255, 0)
    color_teal = (0, 128, 128)
    color_black = (0, 0, 0)
    color_yellow = (255, 255, 0)
    color_violet = (230, 130, 230)
    color_AntiqueWhite = (250, 235, 215)

    A = np.random.randint(0, 3, (num_lines, num_col))

    for i in range(num_col):
      A[0][i] = 5
      A[-1][i] = 4

    for i in range(num_lines):
      A[i][0] = 4
      A[i][-1] = 4


    for i in range(num_lines):
        for j in range(num_col):
            block = None
            y_position = j + offset
            x, y = (i * Block.size, y_position * Block.size)

            if A[i][j] == 0:
                block = Block(color_teal, 10, True, 10, x, y)
            elif A[i][j] == 1:
                block = Block(color_yellow, 10, True, 10, x, y)
            elif A[i][j] == 2:
                block = Block(color_violet, 10, True, 10, x, y)
            elif A[i][j] == 3:
                block = Block(color_AntiqueWhite, 10, True, 10, x, y)
            elif A[i][j] == 4:
                block = Block(color_black, 10, True, 10, x, y)
            elif A[i][j] == 5:
                block = Block(color_green, 10, True, 10, x, y)

            blocks.append(block)

    return blocks


'''def create_map(window_size):
    blocks = []
    block = Block(COLOR['yellow'], 10, True, 10)
    block.create(2 * block.size, 1 * block.size)
    blocks.append(block)
    for i in range(0, window_size[0] // Block.size):
        for j in range(2, window_size[1] // Block.size):
            block = Block(COLOR['yellow'], 10, True, 10, i * Block.size, j * Block.size)
            blocks.append(block)
    return blocks
'''
