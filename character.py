import math
from pygame.draw import *
from pygame.transform import flip
from pygame.image import load
from pygame.transform import scale

color_black = (0, 0, 0)

SCALE = 0.11

SRC_PATH = 'src/'

PLAYER_PATH_Static = 'src/Static.png'
PLAYER_PATH_Going = 'src/Going.png'
PLAYER_PATH_Eating = 'src/Eating.png'
PLAYER_PATH_Jumping = 'src/Jumping.png'
PLAYER_SRC_Static = load(PLAYER_PATH_Static)
PLAYER_SRC_Going = load(PLAYER_PATH_Going)
PLAYER_SRC_Eating = load(PLAYER_PATH_Eating)
PLAYER_SRC_Jumping = load(PLAYER_PATH_Jumping)


class Character:
    '''
    x,y - координаты персонажа
    vx, vy - скорости персонажа по координатам
    g - ускорение свободного падения
    orientation - ориентация картинки персонажа относительно вертикальной оси
    moving_right, moving_left, jump - переменные задающие характер движения
    player_surface_Static (-_Going, -_Eating, -_Jumping) - изображение персонажа во время покоя, ходьбы по горизонтали,
    прыжка и поедания бамбука
    height_no_jump, width_no_jump - высота и ширина изображения персонажа не во время прыжка
    height_jump - высота картинки персонажа во время прыжка
    '''
    x = 200
    y = 50
    vy = 0
    vx = 4
    g = 2

    orientation = False

    moving_right = False
    moving_left = False
    jump = False

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


def up_jump(blocks, screen):
    '''
    :param blocks: массив блоков
    :param screen: экран
    :return: отвечает за перемещение персонажа во время прыжка
    '''
    Character.y -= Character.height_jump - Character.height_no_jump
    x = Character.x
    y = Character.y
    if ((checking_step_capability(x, y - 1 + Character.vy, blocks) and Character.vy < 0)
        and (checking_step_capability(x + Character.width_no_jump, y - 1 + Character.vy,
                                      blocks) and Character.vy < 0)
        or (checking_step_capability(x + Character.width_no_jump,
                                     y + Character.vy + Character.height_jump, blocks) and Character.vy >= 0)
        and (checking_step_capability(x, y + Character.vy + Character.height_jump,
                                      blocks) and Character.vy >= 0)) and Character.jump:
        Character.y += Character.vy
        Character.vy += Character.g
    else:
        if Character.vy > 0:
            Character.jump = False
            Character.y += Character.height_jump - Character.height_no_jump
            tweaking(blocks, screen)
        Character.vy = 0


def tweaking(blocks, screen):
    '''
    :param blocks: массив блоков
    :param screen: экран
    :return: функция отвечает за доводку героя до соприкосновения с ближайшим нижним юлоком после прыжка
    функция необходима, как дополнение к функции up_jump
    '''
    h = 1000
    x = Character.x
    x_new = x + Character.width_no_jump
    y = Character.y + Character.vy + Character.height_no_jump
    for g in blocks:
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


def fall(blocks, screen):
    '''
    :param blocks:
    :param screen:
    :return: функция отвечает за падение персонажа, если под ним нет блоков
    '''
    y0 = Character.y
    tweaking(blocks, screen)
    h = Character.y - y0
    Character.y = y0
    if h != 0 and not Character.jump:
        Character.vy = 0
        Character.jump = True
        up_jump(blocks, screen)


def length(pos, x, y, a):
    '''
    :param pos: координаты клика мыши
    :param x, y: координаты центра квадрата, где нахоится персонаж
    :param a: ширина стороны блока
    :return: определяет находится ли блок, по которому кликнули, рядом с персонажем и возвращает булево значение ответа
    '''
    if (abs(pos[0] - x) < a / 2 and abs(pos[1] - y) < 3 / 2 * a) or (
            abs(pos[0] - x) < 3 * a / 2 and abs(pos[1] - y) < a / 2):
        return True
    else:
        if ((abs(pos[0] - x - a) < a / 2 and abs(pos[1] - y) < 3 / 2 * a) or (
                abs(pos[0] - x - a) < 3 * a / 2 and abs(pos[1] - y) < a / 2)) \
                and (Character.x + Character.width_no_jump > x + a / 2):
            return True
        return False


def nearest_block(x, y, blocks, screen):
    '''
    :param x, y: координаты персонажа
    :param blocks: массив всех блоков
    :param screen: экран
    :return: определяет координаты (x1,y1) центра квадрата, в котором находится левый верхний угол картинки персонажа
             квадрат здесь - это потенциальное место для расположения блока
    '''
    for block in blocks:
        a = block.size
        if (abs(
                block.y - Character.y + screen.get_height() // 2 - y - Character.height_no_jump) < a / 2) and block.x < x < block.x + a:
            x1 = block.x + a / 2
            y1 = block.y - Character.y + screen.get_height() // 2 - a / 2
            return x1, y1
    return x, y


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


def were_to_go(key, blocks, SCORE, screen):
    '''

    :param key: переменная, задающая характер движения
    :param blocks: массив блоков
    :param screen: экран
    :return: Функция задаёт, что делает герой при нажатии на кнопки клавиатуры
    '''
    koef = (math.exp(-1 * (SCORE / 500))) ** 0.5
    if key == 'left' and checking_step_capability(Character.x - Character.vx * koef, Character.y, blocks) and \
            checking_step_capability(Character.x - Character.vx * koef, Character.y + Character.height_no_jump - 2,
                                     blocks):
        Character.x -= Character.vx * koef
    if key == 'right' and \
            checking_step_capability(Character.x + Character.vx * koef + Character.width_no_jump, Character.y,
                                     blocks) and \
            checking_step_capability(Character.x + Character.vx * koef + Character.width_no_jump,
                                     Character.y + Character.height_no_jump - 2, blocks):
        Character.x += Character.vx * koef
    if key == 'jump':
        Character.vy = -10


def draw_p(screen, image):
    '''
    :param screen: экран
    :param image: номер картинки персонажа, которую необходимо отобразить на экарне
    :return: отрисовывает необходимую картинку персонажа на экране
    '''
    if image == 0:
        screen.blit(flip(Character.player_surface_Static, Character.orientation, False),
                    (Character.x, screen.get_height() // 2))
    if image == 1:
        screen.blit(flip(Character.player_surface_Going, Character.orientation, False),
                    (Character.x, screen.get_height() // 2))
    if image == 2:
        screen.blit(flip(Character.player_surface_Eating, Character.orientation, False),
                    (Character.x, screen.get_height() // 2))
    if image == 3:
        screen.blit(flip(Character.player_surface_Jumping, Character.orientation, False),
                    (Character.x, screen.get_height() // 2))


def draw(screen, phase_1, phase_2):
    '''
    :param screen: экран
    :param phase_1: счётчик кадров в виде числа, остаток от деления на 2 разряда десятков которого определяет,
                    какое изображение из двух сменяющихся должно быть на экране
    :param phase_2: параметр, задающий ест ли сейчас персонаж (phase_2=1) или нет ((phase_2=0)
    :return: функция определяет какое именно изображение персонажа надо вывести на экран в данный момент
    '''
    m = int(phase_1 / 5)
    if phase_2 == 0:
        if m % 2 == 1:
            draw_p(screen, 0)
        else:
            draw_p(screen, 1)
    else:
        if m % 2 == 0:
            draw_p(screen, 0)
        else:
            draw_p(screen, 2)


if __name__ == "__main__":
    print("This module is not for direct call!")
