from pygame.draw import *
import pygame
import numpy as np
from pygame.image import load
from pygame.transform import scale
from character import *
from os import listdir, getcwd
from os.path import isfile, join
from random import randint

COLOR = {
    'green': (0, 255, 0),
    'yellow': (255, 255, 0)
}
BLOCK_SIZE = 50
PLAYER_PATH_Static = 'src/Static.png'
PLAYER_PATH_Going = 'src/Going.png'
PLAYER_PATH_Eating = 'src/Eating.png'
PLAYER_PATH_Jumping = 'src/Jumping.png'
PLAYER_SRC_Static = load(PLAYER_PATH_Static)
PLAYER_SRC_Going = load(PLAYER_PATH_Going)
PLAYER_SRC_Eating = load(PLAYER_PATH_Eating)
PLAYER_SRC_Jumping = load(PLAYER_PATH_Jumping)

SCALE = 0.11

SRC_PATH = 'src/'
BLOCKS_PATH = SRC_PATH + "blocks/"


OS_BLOCK_PATH = getcwd() + "\\" + BLOCKS_PATH.replace("/", "\\")[:-1]

BLOCK_NAMES = [f[:-4] for f in listdir(OS_BLOCK_PATH) if isfile(join(OS_BLOCK_PATH, f))]

BLOCKS_SRC = {
    name:scale(load(BLOCKS_PATH + name + ".png"), (BLOCK_SIZE, BLOCK_SIZE)) for name in BLOCK_NAMES
}

class Character:
    x = 200
    y = 50
    vy = 0
    vx = 2
    g = 1
    hp = 10
    attack_range = 50

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
    size = BLOCK_SIZE

    def __init__(self, name, hp, breakable, loot, x, y, passable=False):
        self.id = name

        self.img = BLOCKS_SRC[name]
        self.hp = hp
        self.breakable = breakable
        self.loot = loot  # ochkov
        self.x = x
        self.y = y

    def create(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, phl):  # player height level
        # rect(screen, self.color, (self.x, self.y, self.size, self.size))
        screen.blit(self.img, (self.x, self.y - phl + screen.get_height() // 2))

    def kill(self, blocks):
        blocks.remove(self)

    def damage(self):
        if self.breakable == True:
            self.hp -= 5


def create_map(window_size, offset=2):
    blocks = []
    num_lines = window_size[0] // BLOCK_SIZE
    num_col = window_size[1] // BLOCK_SIZE * 2

    # A = np.random.randint(0, 3, (num_lines, num_col)) # Дань уважения войнам погибшим при битве за Сталинград

    for i in range(-4, num_col):
        y_position = i + offset
        x_start, y, x_end = -1 * BLOCK_SIZE, y_position * BLOCK_SIZE, num_lines * BLOCK_SIZE
        blocks.append(Block("$bedrock", 1, False, 1, x_start, y))
        blocks.append(Block("$bedrock", 1, False, 1, x_end, y))

    for i in range(num_lines):
        for j in range(num_col + 4):
            y_position = j + offset
            x, y = i * BLOCK_SIZE, y_position * BLOCK_SIZE

            if j == num_col - 1:
                block = Block("$bedrock", 1, False, 1, x, y)
            elif j >= num_col:
                block = Block("$under_bedrock", 1, False, 1, x, y)
            else:
                name = BLOCK_NAMES[randint(BLOCK_NAMES.index("$under_bedrock") + 1, len(BLOCK_NAMES) - 1)]
                block = Block(name, 1, True, 10, x, y)
            """
            if A[i][j] == 0:
                block = Block(COLOR['teal'], 10, True, 10, x, y)   
            elif A[i][j] == 1:
                block = Block(COLOR['yellow'], 10, True, 10, x, y)
            elif A[i][j] == 2:
                block = Block(COLOR['violet'], 10, True, 10, x, y)
            elif A[i][j] == 3:
                block = Block(COLOR['AntiqueWhite'], 10, True, 10, x, y)
            elif A[i][j] == 4:
                block = Block(COLOR['black'], 10, True, 10, x, y)
            elif A[i][j] == 5:
                block = Block(COLOR['green'], 10, True, 10, x, y)
            """
            if (randint(0, 10) > 7):
                blocks.append(Block("$$liana", 1, False, 1, x, y, True))
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
    return blocks'''
