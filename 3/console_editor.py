#!/usr/bin/env python3
'''
Хохлов Андрей

'''
import os
import re
import json

import turtle as t


# Сообщения редактора
wellcome_msg = '''
Вас приветствует Turtle Console Editor!

Меню:
Чтобы нарисовать фигуру - введите 1
Чтобы открыть файл с данными фигуры - введите 2

Чтобы выйти из редактора - введите 0
'''

fig_msg = '''
Выберите фигуру из списка:
Правильнык треугольник - введите 1
Квадрат - введите 2
Прямоугольник - введите 3
Окружность - введите 4

В главное меню - введите 0
'''


def _goto(begin):
    t.up()
    t.goto(*begin)
    t.down()


def draw_triangle(begin, side, group=False):
    _goto(begin)
    t.forward(side)
    x = begin[0]+(side/2)
    y = round(begin[1]+0.866025*side)
    t.goto(x, y)
    t.goto(*begin)
    if not group:
        t.exitonclick()


def draw_square(begin, side, group=False):
    _goto(begin)
    for _ in range(4):
        t.forward(side)
        t.left(90)
    if not group:
        t.exitonclick()


def draw_rectangle(begin, diagonal_point, group=False):
    _goto(begin)
    for _ in range(2):
        t.forward(diagonal_point[0])
        t.left(90)
        t.forward(diagonal_point[1])
        t.left(90)
    if not group:
        t.exitonclick()


def draw_circle(begin, radius, group=False):
    t.up()
    t.goto(*begin)
    t.forward(radius)
    t.down()
    t.left(90)
    t.circle(radius)
    if not group:
        t.exitonclick()


if __name__ == '__main__':
    print(wellcome_msg)

    while True:
        resp = input('--->  ')

        if resp == '0':
            print('Пока!')
            exit()

        elif resp == '1':
            print(fig_msg)
            fig = int(input('--->  '))

            # Если выбран треугольник или окружность
            if fig == 1 or fig == 2:
                while True:
                    begin = input('Введите координаты левой нижней вершины в формате: x,y ---> ')
                    if not re.match(r'[0-9]+,[0-9]+', begin):
                        continue
                    side = input('Введите длину стороны: ---> ')
                    if not side.isnumeric():
                        continue
                    begin = [int(x) for x in begin.split(',')]
                    side = int(side)
                    if fig == 1:
                        draw_triangle(begin, side)
                    else:
                        draw_square(begin, side)
                    print(wellcome_msg)
                    break

            # Если выбран прямоугольник
            if fig == 3:
                while True:
                    begin = input('Введите координаты левой нижней вершины в формате: x,y ---> ')
                    if not re.match(r'[0-9]+,[0-9]+', begin):
                        continue
                    diagonal_point = input('Введите координаты диагонально противоположной вершины в формате: x,y ---> ')
                    if not re.match(r'[0-9]+,[0-9]+', diagonal_point):
                        continue
                    begin = [int(x) for x in begin.split(',')]
                    diagonal_point = [int(x) for x in diagonal_point.split(',')]
                    draw_rectangle(begin, diagonal_point)
                    print(wellcome_msg)
                    break

            # Если выбрана окружность
            if fig == 4:
                while True:
                    begin = input('Введите координаты центра в формате: x,y ---> ')
                    if not re.match(r'[0-9]+,[0-9]+', begin):
                        continue
                    radius = input('Введите радиус: ---> ')
                    if not radius.isnumeric():
                        continue
                    begin = [int(x) for x in begin.split(',')]
                    radius = int(radius)
                    draw_circle(begin, radius)
                    print(wellcome_msg)
                    break

            # Возврат в главное меню
            if fig == 0:
                print(wellcome_msg)
                continue

        # Если данные читаются из файла
        elif resp == '2':
            while True:
                file = input('Введите полный путь к файлу. Пример: /home/user/file.txt --->  ')
                if os.path.isfile(file):
                    break
            try:
                content = json.load(open(file))
            except ValueError:
                print("Неверный синтаксис файла!")
                content = None

            if content:
                for figure, data in content.items():
                    if figure == 'triangle':
                        draw_triangle(data['begin'], data['side'], group=True)
                    if figure == 'square':
                        draw_square(data['begin'], data['side'], group=True)
                    if figure == 'rectangle':
                        draw_rectangle(data['begin'], data['diagonal_point'], group=True)
                    if figure == 'circle':
                        draw_circle(data['begin'], data['radius'], group=True)
                else:
                    t.exitonclick()
            print(wellcome_msg)

        else:
            print("Неверное значение. Повторите еще раз.")
