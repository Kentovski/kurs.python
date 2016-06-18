#!/usr/bin/env python3

'''
Хохлов Андрей

'''

from functools import reduce

'''
piramid = (
    (00, ),
    (10, 11),
    (20, 21, 22),
    (30, 31, 32, 33)
)
'''
piramid = (
    (1, ),
    (2, 1),
    (1, 2, 1),
    (1, 2, 1, 1),
    (1, 2, 1, 1, 1),
    (1, 2, 1, 1, 1, 1),
    (1, 2, 1, 1, 1, 9, 1),
)

'''
piramid = (
    (7, ),
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    (3, 1, 3, 1, 3),
    (2, 2, 2, 2, 2, 2),
    (5, 6, 4, 5, 6, 4, 3),
)
'''


def shift(arg):
    '''
    Функция накопительного суммирования.
    Это более понятная версия этого генератора:
    [0] + [ reduce(lambda x, y: x + y, z) for z in
    [list(d[:t]) for t in range(1, len(arg) + 1)]
    ]
    '''
    res = []
    z = []
    for t in range(1, len(arg) + 1):
        z.append(arg[:t])

    for k in z:
        res.append(reduce(lambda x, y: x + y, k))
    return [0] + res


def calc_var(var):
    '''
    Подсчитывает сумму всех элементов
    одного варианта
    '''
    c = []
    for row in range(len(piramid)):
        c.append(piramid[row][var[row]])
    return sum(c)

if __name__ == '__main__':
    iterations = [i for i in [[0, 1], ]] * (len(piramid))
    res = [[]]
    for iter_ in iterations:
        res = [i+[j] for i in res for j in iter_]

    # Индексы всех вариантов, которые возможны в данной пирамиде
    indexes = [shift(arg) for arg in res]

    max_sum = max([calc_var(var) for var in indexes])
    print('Максимальная сумма равна: %s' % max_sum)
