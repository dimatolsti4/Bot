import pygame
from chtoto import Block, Character
from pygame.draw import *
from pygame.transform import flip

color_black = (0, 0, 0)


def up_jump(bl, display):
    '''

    :param bl: массив блоков
    :param display: экран
    :return: отвечает за перемещение персонажа во время прыжка
    '''
    x = Character.x
    y = Character.y
    if ((checking_step_capability(x, y - 1 + Character.vy, bl) and Character.vy < 0)
        and (checking_step_capability(x + Character.player_surface.get_width(), y - 1 + Character.vy,
                                      bl) and Character.vy < 0)
        or (checking_step_capability(x + Character.player_surface.get_width(),
                                     y + Character.vy + Character.player_surface.get_width(), bl) and Character.vy >= 0)
        and (checking_step_capability(x, y + Character.vy + Character.player_surface.get_width(),
                                      bl) and Character.vy >= 0)) and Character.jump:
        Character.y += Character.vy
        circle(display, (255, 0, 255), (Character.x, Character.y), 5)
        Character.vy += Character.g
    else:
        if Character.vy > 0:
            Character.jump = False
            tweaking(bl, display)
        Character.vy = 0


def tweaking(bl, display):
    '''

    :param bl: массив блоков
    :param display: экран
    :return: функция отвечает за доводку героя до соприкосновения с ближайшим нижним юлоком после прыжка
    функция необходима, как дополнение к функции up_jump
    '''
    h = 1000
    x = Character.x
    x_new = x + Character.player_surface.get_width()
    y = Character.y + Character.vy + Character.player_surface.get_width()
    for g in bl:
        if cross_product(g.x, g.y, g.x + g.size, g.y, x, y) \
                and cross_product(g.x + g.size, g.y, g.x + g.size, g.y + g.size, x, y) \
                and cross_product(g.x + g.size, g.y + g.size, g.x, g.y + g.size, x, y) \
                and cross_product(g.x, g.y + g.size, g.x, g.y, x, y) \
                or cross_product(g.x, g.y, g.x + g.size, g.y, x_new, y) \
                and cross_product(g.x + g.size, g.y, g.x + g.size, g.y + g.size, x_new, y) \
                and cross_product(g.x + g.size, g.y + g.size, g.x, g.y + g.size, x_new, y) \
                and cross_product(g.x, g.y + g.size, g.x, g.y, x_new, y):
            m = g.y - y + Character.vy
            if h > m:
                h = m
            break
    Character.y += h


def fall(bl, display):
    '''

    :param bl:
    :param display:
    :return: функция отвечает за падение персонажа, если под ним нет блокав
    '''
    y0 = Character.y
    tweaking(bl, display)
    h = Character.y - y0
    Character.y = y0
    if h != 0 and not Character.jump:
        Character.vy = 0
        Character.jump = True
        up_jump(bl, display)


def break_block(pos, x, y, blocks):
    '''
    Функция проверяет можно ли сломать блок и есть ли он вообще в месте клика
    если g.type ==1 то блок сломать можно
    '''
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


def length(pos, x, y, a):
    '''
    Функция проверяет, находится ли блок рядом с персонажем
    x,y - координаты персонажа
    a -длина стороны блока
    pos - координаты клика
    '''
    if (abs(pos[0] - x) < a / 2 and abs(pos[1] - y) < 3 / 2 * a) or (
            abs(pos[0] - x) < 3 * a / 2 and abs(pos[1] - y) < a / 2):
        return True
    else:
        return False


def cross_product(x1, y1, x2, y2, x0, y0):
    '''
    Функция определяет знак векторного произведения двух векторов
    x0,y0 - координаты первого вектора в СК экрана
    x2,y2 - координаты второго вектора в СК экрана
    x1,y1 - координаты центра СК относительно которой мы рассматриваем концы векторов 1 и 2
    '''
    if (x0 - x1) * (y2 - y1) - (x2 - x1) * (y0 - y1) <= 0:
        return True
    else:
        return False


def checking_step_capability(x, y, blocks):
    '''
    Функция проверяет, есть ли блок в направлении, куда хочет пойти игрок
    x,y - координаты, куда хочет попасть игрок
    blocks - массив блоков
    '''
    for g in blocks:
        if cross_product(g.x, g.y, g.x + g.size, g.y, x, y) \
                and cross_product(g.x + g.size, g.y, g.x + g.size, g.y + g.size, x, y) \
                and cross_product(g.x + g.size, g.y + g.size, g.x, g.y + g.size, x, y) \
                and cross_product(g.x, g.y + g.size, g.x, g.y, x, y):
            return False

    return True


def were_to_go(k, bl, display):
    '''
    Функция задаёт, что делает герой при нажатии на кнопки клавиатуры
    '''
    if k == 'left' and checking_step_capability(Character.x - Character.vx, Character.y, bl) and \
            checking_step_capability(Character.x - Character.vx, Character.y + Character.player_surface.get_width() - 2,
                                     bl):
        Character.x -= Character.vx
    if k == 'right' and \
            checking_step_capability(Character.x + Character.vx + Character.player_surface.get_width(), Character.y,
                                     bl) and \
            checking_step_capability(Character.x + Character.vx + Character.player_surface.get_width(),
                                     Character.y + Character.player_surface.get_width() - 2, bl):
        Character.x += Character.vx
    if k == 'jump':
        Character.vy = -10


def draw_p(screen):
    screen.blit(flip(Character.player_surface, Character.orientation, False), (Character.x, Character.y))


if __name__ == "__main__":
    print("This module is not for direct call!")