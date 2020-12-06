from pygame.draw import *
import pygame
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


def create_map(window_size):
    blocks = []
    block = Block(COLOR['yellow'], 10, True, 10)
    block.create(2 * block.size, 1 * block.size)
    blocks.append(block)
    for i in range(0, window_size[0] // Block.size):
        for j in range(2, window_size[1] // Block.size):
            block = Block(COLOR['yellow'], 10, True, 10)
            block.create(i * block.size, j * block.size)
            blocks.append(block)
    return blocks
