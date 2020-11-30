from game_objects import Blocks, Character

def break_block(pos, x, y):
    if ()

def destroy_block(pos):

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
        else:
            return True
'''
Функция проверяет, есть ли блок в направлении, куда хочет пойти игрок
x,y - координаты, куда хочет попасть игрок
blocks - массив блоков
'''


def what_to_do(event, blocks):
    if event.type == pygame.KEYDOWN:
        if event.kiy == pygame.K_a and checking_step_capability(Character.x - Character.vx, Character.y, blocks):
            Character.x -= Character.vx
        if event.kiy == pygame.K_d and checking_step_capability(Character.x + Character.vx, Character.y, blocks):
            Character.x += Character.vx
        if event.kiy == pygame.K_w and checking_step_capability(Character.x, Character.y - Character.vy, blocks):
            Character.y -= Character.vy
        if event.kiy == pygame.K_s and checking_step_capability(Character.x, Character.y + Character.vy, blocks):
            Character.y += Character.vy
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if break_block(event.pos, Character.x, Character.y):
            destroy_block(event.pos)
'''
Функция задаёт, что делает герой при нажатии на кнопки управления
'''


if __name__ == "__main__":
    print("This module is not for direct call!")
