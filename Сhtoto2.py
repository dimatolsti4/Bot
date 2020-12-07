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


'''def draw(self):
    global display
    pygame.rect(display, self.color, (self.x, self.y, self.x_size, self.y_size))'''


class Block():
    size = 50

    def __init__(self, color, hp, breakable, loot):
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
            self.hp -= 1


def create_map():
    blocks = []
    color_green = (0, 255, 0)
    color_teal = (0, 128, 128)
    color_black = (255, 255, 255)
    color_yellow = (255, 255, 0)
    color_violet = (230, 130, 230)
    color_AntiqueWhite = (250, 235, 215)
    A = np.random.randint(0, 3, (120))

    A[0] = 4
    A[12] = 4
    A[13] = 4
    A[24] = 4
    A[25] = 4   
    A[36] = 4
    A[37] = 4
    A[48] = 4
    A[49] = 4
    A[60] = 4
    A[61] = 4
    A[72] = 4
    A[73] = 4
    A[84] = 4
    A[85] = 4
    A[96] = 4
    A[97] = 4

    for i in range(0, 97):
        if 0 <= i <= 13:
            if A[i] == 0:
                block = Block(color_green, 10, True, 10)
                block.create(i * block.size, 3 * block.size)
                blocks.append(block)
            else:
                if A[i] == 1:
                    block = Block(color_green, 10, True, 10)
                    block.create(i * block.size, 3 * block.size)
                    blocks.append(block)
                else:
                    if A[i] == 2:
                        block = Block(color_green, 10, True, 10)
                        block.create(i * block.size, 3 * block.size)
                        blocks.append(block)
                    else:
                        if A[i] == 3:
                            block = Block(color_green, 10, True, 10)
                            block.create(i * block.size, 3 * block.size)
                            blocks.append(block)
                        else:
                            if A[i] == 4:
                                block = Block(color_green, 10, True, 10)
                                block.create(i * block.size, 3 * block.size)
                                blocks.append(block)
        else:
            if 13 <= i <= 25:
                if A[i] == 0:
                    block = Block(color_teal, 10, True, 10)
                    block.create((i-13) * block.size, 4 * block.size)
                    blocks.append(block)
                else:
                    if A[i] == 1:
                        block = Block(color_yellow, 10, True, 10)
                        block.create((i-13) * block.size, 4 * block.size)
                        blocks.append(block)
                    else:
                        if A[i] == 2:
                            block = Block(color_violet, 10, True, 10)
                            block.create((i-13) * block.size, 4 * block.size)
                            blocks.append(block)
                        else:
                            if A[i] == 3:
                                block = Block(color_AntiqueWhite, 10, True, 10)
                                block.create((i-13) * block.size, 4 * block.size)
                                blocks.append(block)
                            else:
                                if A[i] == 4:
                                    block = Block(color_black, 10, True, 10)
                                    block.create((i-13) * block.size, 4 * block.size)
                                    blocks.append(block)
            else:
                if 25 <= i <= 37:
                    if A[i] == 0:
                        block = Block(color_teal, 10, True, 10)
                        block.create((i-25) * block.size, 5 * block.size)
                        blocks.append(block)
                    else:
                        if A[i] == 1:
                            block = Block(color_yellow, 10, True, 10)
                            block.create((i-25) * block.size, 5 * block.size)
                            blocks.append(block)
                        else:
                            if A[i] == 2:
                                block = Block(color_violet, 10, True, 10)
                                block.create((i-25) * block.size, 5 * block.size)
                                blocks.append(block)
                            else:
                                if A[i] == 3:
                                    block = Block(color_AntiqueWhite, 10, True, 10)
                                    block.create((i-25) * block.size, 5 * block.size)
                                    blocks.append(block)
                                else:
                                    if A[i] == 4:
                                        block = Block(color_black, 10, True, 10)
                                        block.create((i-25) * block.size, 5 * block.size)
                                        blocks.append(block)
                else:
                    if 37 <= i <= 49:
                        if A[i] == 0:
                            block = Block(color_teal, 10, True, 10)
                            block.create((i-37) * block.size, 6 * block.size)
                            blocks.append(block)
                        else:
                            if A[i] == 1:
                                block = Block(color_yellow, 10, True, 10)
                                block.create((i-37) * block.size, 6 * block.size)
                                blocks.append(block)
                            else:
                                if A[i] == 2:
                                    block = Block(color_violet, 10, True, 10)
                                    block.create((i-37) * block.size, 6 * block.size)
                                    blocks.append(block)
                                else:
                                    if A[i] == 3:
                                        block = Block(color_AntiqueWhite, 10, True, 10)
                                        block.create((i-37) * block.size, 6 * block.size)
                                        blocks.append(block)
                                    else:
                                        if A[i] == 4:
                                            block = Block(color_black, 10, True, 10)
                                            block.create((i-37) * block.size, 6 * block.size)
                                            blocks.append(block)
                    else:
                        if 49 <= i <= 61:
                            if A[i] == 0:
                                block = Block(color_teal, 10, True, 10)
                                block.create((i-49) * block.size, 7 * block.size)
                                blocks.append(block)
                            else:
                                if A[i] == 1:
                                    block = Block(color_yellow, 10, True, 10)
                                    block.create((i-49) * block.size, 7 * block.size)
                                    blocks.append(block)
                                else:
                                    if A[i] == 2:
                                        block = Block(color_violet, 10, True, 10)
                                        block.create((i-49) * block.size, 7 * block.size)
                                        blocks.append(block)
                                    else:
                                        if A[i] == 3:
                                            block = Block(color_AntiqueWhite, 10, True, 10)
                                            block.create((i-49) * block.size, 7 * block.size)
                                            blocks.append(block)
                                        else:
                                            if A[i] == 4:
                                                block = Block(color_black, 10, True, 10)
                                                block.create((i-49) * block.size, 7 * block.size)
                                                blocks.append(block)
                        else:
                            if 61 <= i <= 73:
                                if A[i] == 0:
                                    block = Block(color_teal, 10, True, 10)
                                    block.create((i-61) * block.size, 8 * block.size)
                                    blocks.append(block)
                                else:
                                    if A[i] == 1:
                                        block = Block(color_yellow, 10, True, 10)
                                        block.create((i-61) * block.size, 8 * block.size)
                                        blocks.append(block)
                                    else:
                                        if A[i] == 2:
                                            block = Block(color_violet, 10, True, 10)
                                            block.create((i-61) * block.size, 8 * block.size)
                                            blocks.append(block)
                                        else:
                                            if A[i] == 3:
                                                block = Block(color_AntiqueWhite, 10, True, 10)
                                                block.create((i-61) * block.size, 8 * block.size)
                                                blocks.append(block)
                                            else:
                                                if A[i] == 4:
                                                    block = Block(color_black, 10, True, 10)
                                                    block.create((i-61) * block.size, 8 * block.size)
                                                    blocks.append(block)
                            else:
                                if 73 <= i <= 85:
                                    if A[i] == 0:
                                        block = Block(color_teal, 10, True, 10)
                                        block.create((i-73) * block.size, 9 * block.size)
                                        blocks.append(block)
                                    else:
                                        if A[i] == 1:
                                            block = Block(color_yellow, 10, True, 10)
                                            block.create((i-73) * block.size, 9 * block.size)
                                            blocks.append(block)
                                        else:
                                            if A[i] == 2:
                                                block = Block(color_violet, 10, True, 10)
                                                block.create((i-73) * block.size, 9 * block.size)
                                                blocks.append(block)
                                            else:
                                                if A[i] == 3:
                                                    block = Block(color_AntiqueWhite, 10, True, 10)
                                                    block.create((i-73) * block.size, 9 * block.size)
                                                    blocks.append(block)
                                                else:
                                                    if A[i] == 4:
                                                        block = Block(color_black, 10, True, 10)
                                                        block.create((i-73) * block.size, 9 * block.size)
                                                        blocks.append(block)
                                else:
                                    if 85 <= i <= 97:
                                        if A[i] == 0:
                                            block = Block(color_black, 10, True, 10)
                                            block.create((i-85) * block.size, 10 * block.size)
                                            blocks.append(block)
                                        else:
                                            if A[i] == 1:
                                                block = Block(color_black, 10, True, 10)
                                                block.create((i-85) * block.size, 10 * block.size)
                                                blocks.append(block)
                                            else:
                                                if A[i] == 2:
                                                    block = Block(color_black, 10, True, 10)
                                                    block.create((i-85) * block.size, 10 * block.size)
                                                    blocks.append(block)
                                                else:
                                                    if A[i] == 3:
                                                        block = Block(color_black, 10, True, 10)
                                                        block.create( (i-85) * block.size, 10 * block.size)
                                                        blocks.append(block)
    return blocks


'''def create_map(window_size):
    blocks = []
    block = Block(COLOR['yellow'], 10, True, 10)
    block.create(2 * block.size, 1 * block.size)
    blocks.append(block)
    for i in range(0, window_size[0] // Block.size):
        for j in range(2, window_size[1] // Block.size):
            block = Block(COLOR['yellow'], 10, True, 10)
            block.create(i * block.size, j * block.size)
            blocks.append(block)
    return blocks'''
