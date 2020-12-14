from pygame.draw import *
import pygame
import numpy as np
from pygame.image import load
from pygame.transform import scale
from character import *
from os import listdir, getcwd
from os.path import isfile, join
from random import randint

BLOCK_SIZE = 50
SCREEN_HEIGHT = 1200

SRC_PATH = 'src/'
BLOCKS_PATH = SRC_PATH + "blocks/"

OS_BLOCK_PATH = getcwd() + "\\" + BLOCKS_PATH.replace("/", "\\")[:-1]

BLOCK_NAMES = [f[:-4] for f in listdir(OS_BLOCK_PATH) if isfile(join(OS_BLOCK_PATH, f))]

BLOCKS_SRC = {name: scale(load(BLOCKS_PATH + name + ".png"), (BLOCK_SIZE, BLOCK_SIZE)) for name in BLOCK_NAMES}
BLOCK_POINTS = {
    "bamboo": 10,
    "bambooo": 50,
    "diamond": 100
}

class Block():
    size = BLOCK_SIZE

    def __init__(self, name, hp, breakable, points, x, y, use, passable=False):
        """
        Method-initializator: returns void
        name:      string <block name>
        hp:        int    <how many hits to break block>
        breakable: bool   <is block breakable> ##
        points:    int    <how many points you get by breaking>
        x, y:      int    <block coords>
        use:       pass   <undefined>
        passable   bool   <is block passable> ##
        """
        self.id = name

        self.img = BLOCKS_SRC[self.id]
        self.hp = hp
        self.breakable = breakable
        self.points = points
        self.x = x
        self.y = y
        self.use = use

    def draw(self, screen, phl):
        """
        Draw block on screen according to player height: returns void
        screen: pygame.Display <Game display class>
        phl:    int            <Player y coord>
        """
        screen.blit(self.img, (self.x, self.y - phl + screen.get_height() // 2))

    def kill(self, blocks, SCORE):
        """
        Removes block from list of blocks when destroyed: returns int
        blocks: list<Block> <List of blocks>
        SCORE:  int         <Current score>
        """
        blocks.remove(self)
        return SCORE + self.points

    def damage(self):
        """
        damages block: returns void
        """
        if self.breakable == True:
            self.hp -= 1
            if self.id == "bamboo":
                self.img = BLOCKS_SRC["$$$bamboo_break"]
            if self.id == "bambooo":
                self.img = BLOCKS_SRC["$$$bambooo_break"]
            if self.id == "diamond":
                self.img = BLOCKS_SRC["$$$diamond_break"]


def create_map(window_size, offset=2):
    """
    creates map of blocks: returns list<Block>
    window_size: int <screen metrics>
    offset:      int <number of blank lines on the top of the screen>
    """
    blocks = []
    num_lines = window_size[0] // Block.size
    num_col = SCREEN_HEIGHT // Block.size * 2
    
    for i in range(-4, num_col):
        y_position = i + offset
        x_start, y, x_end = -1 * Block.size, y_position * Block.size, num_lines * Block.size
        blocks.append(Block("$bedrock", 1, False, 0, x_start, y, 0))
        blocks.append(Block("$bedrock", 1, False, 0, x_end, y, 0))

    for i in range(num_lines):
        for j in range(num_col + 4):
            y_position = j + offset
            x, y = i * Block.size, y_position * Block.size

            if j == num_col - 1:
                block = Block("$bedrock", 1, False, 0, x, y, 0)
            elif j >= num_col:
                block = Block("$under_bedrock", 1, False, 0, x, y, 0)
            elif j <= num_col // 2:
                name = BLOCK_NAMES[randint(BLOCK_NAMES.index("$under_bedrock") + 1, len(BLOCK_NAMES) - 2)]
                block = Block(name, 70, True, BLOCK_POINTS[name], x, y, 0)
            else:
                name = BLOCK_NAMES[randint(BLOCK_NAMES.index("$under_bedrock") + 1, len(BLOCK_NAMES) - 1)]
                block = Block(name, 70, True, BLOCK_POINTS[name], x, y, 0)
            if (randint(0, 10) > 7):
                blocks.append(Block("$$liana", 1, False, 0, x, y, 0, True))
            blocks.append(block)

    return blocks
