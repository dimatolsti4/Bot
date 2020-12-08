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
PLAYER_PATH = 'src/player.jpg'
PLAYER_SRC = load(PLAYER_PATH)

SCALE = 0.1


class Character:
    x = 200
    y = 75
    vy = 0
    vx = 3
    g = 1
    hp = 10

    orientation = False

    moving_right = False
    moving_left = False
    jump = False

    color = (255, 255, 255)

    player_surface = scale(PLAYER_SRC, (int(PLAYER_SRC.get_width() * SCALE), int(PLAYER_SRC.get_height() * SCALE)))


class Block():
    size = 50

    def __init__(self, color, hp, breakable, loot, x, y):
        self.color = color
        self.hp = hp
        self.breakable = breakable
        self.loot = loot  # ochkov
        self.x = x
        self.y = y

    def draw(self, screen):
        rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def kill(self, blocks):
        blocks.remove(self)

    def damage(self):
        if self.breakable == True:
            self.hp -= 1


def create_map(num_lines, num_col, offset=2):
    blocks = []
    color_green = (0, 255, 0)
    A = np.random.randint(0, 3, (num_lines, num_col))
		
    for i in range(num_col):
      A[offset][i] = 5
      A[-1][i] = 4
      
    for i in range(num_lines):
      A[i][0] = 4
      A[i][-1] = 4

    
    for i in range(num_lines):
        for j in range(num_col):
          	block = None
            y_position = j + offset
            x, y = (i * block.size, y_position * block.size)
            
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
