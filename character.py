import pygame
from game_objects import Blocks, Character
from pygame.draw import *


def up_jump(bl, display, jump):
    if checking_step_capability(Character.x, Character.y + Character.vy, bl):
        Character.y += Character.vy
        circle(display, (255, 0, 255), (Character.x, Character.y), 5)
        Character.vy += Character.g
    else:
        if Character.vy > 0:
            jump = False
        Character.vy = 0


def break_block(pos, x, y, blocks):
    for g in blocks:
        if cross_product(g.x, g.y, g.x + g.a, g.y, pos[0], pos[1]) \
                and cross_product(g.x + g.a, g.y, g.x + g.a, g.y + g.a, pos[0], pos[1]) \
                and cross_product(g.x + g.a, g.y + g.a, g.x, g.y + g.a, pos[0], pos[1]) \
                and cross_product(g.x, g.y + g.a, g.x, g.y, pos[0], pos[1]):
            if g.type == 1 and length(pos, x, y, g.a):
                return True
            else:
                return False
    return False


'''
Функция проверяет можно ли сломать блок и есть ли он вообще в месте клика
если g.type ==1 то блок сломать можно
'''


def length(pos, x, y, a):
    if (abs(pos[0] - x) < a / 2 and abs(pos[1] - y) < 3 / 2 * a) or (
            abs(pos[0] - x) < 3 * a / 2 and abs(pos[1] - y) < a / 2):
        return True
    else:
        return False


'''
Функция проверяет, находится ли блок рядом с персонажем
x,y - координаты персонажа
a -длина стороны блока
pos - координаты клика
'''


def destroy_block(pos):
    c = 0


def cross_product(x1, y1, x2, y2, x0, y0):
    if (x0 - x1) * (y2 - y1) - (x2 - x1) * (y0 - y1) >= 0:
        return True
    else:
        return False


'''
Функция определяет знак векторного произведения двух векторов
x0,y0 - координаты первого вектора в СК экрана
x2,y2 - координаты второго вектора в СК экрана
x1,y1 - координаты центра СК относительно которой мы рассматриваем концы векторов 1 и 2
'''


def checking_step_capability(x, y, blocks):
    for g in blocks:
        if cross_product(g.x, g.y, g.x + g.a, g.y, x, y) \
                and cross_product(g.x + g.a, g.y, g.x + g.a, g.y + g.a, x, y) \
                and cross_product(g.x + g.a, g.y + g.a, g.x, g.y + g.a, x, y) \
                and cross_product(g.x, g.y + g.a, g.x, g.y, x, y):
            return False
    return True


'''
Функция проверяет, есть ли блок в направлении, куда хочет пойти игрок
x,y - координаты, куда хочет попасть игрок
blocks - массив блоков
'''


def were_to_go(k, bl, display):
    if k == 'left' and checking_step_capability(Character.x - Character.vx, Character.y, bl):
        Character.x -= Character.vx
    if k == 'right' and checking_step_capability(Character.x + Character.vx, Character.y, bl):
        Character.x += Character.vx
    if k == 'jump':
        Character.vy = -10


'''
Функция задаёт, что делает герой при нажатии на кнопки клавиатуры
'''


def draw(c, display):
    if c == 0:
        circle(display, (255, 0, 255), (Character.x, Character.y), 5)
    else:
        rect(display, (155, 100, 255), (Character.x, Character.y, 5, 5))


def what_to_do(event, bl, display):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if break_block(event.pos, Character.x, Character.y, bl):
            destroy_block(event.pos)


'''
Функция задаёт, что делает герой при нажатии на кнопку мыши
'''

if __name__ == "__main__":
    print("This module is not for direct call!")
