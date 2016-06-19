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
Чтобы открыть файл с данными фигуры и построить ее - введите 2
Чтобы открыть и отредактировать файл фигуры - введите 3
Чтобы создать новый файл с фигурой(ми) - введите 4

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

add_fig_msg = '''
Выберите фигуру, которую нужно добавить:
Правильнык треугольник - введите 1
Квадрат - введите 2
Прямоугольник - введите 3
Окружность - введите 4

Записать все фигуры в файл - введите 9
В главное меню - введите 0
'''


class Figure(object):
    """Главный класс получения и постороения фигур"""

    def _goto(self, begin):
        t.up()
        t.goto(*begin)
        t.down()

    def get(self, type):
        if type == 'triangle':
            while True:
                begin = input('Введите координаты левой нижней вершины в формате: x,y ---> ')
                if not re.match(r'[0-9]+,[0-9]+', begin):
                    continue
                side = input('Введите длину стороны: ---> ')
                if not side.isnumeric():
                    continue
                else:
                    break
            return {"type": "triangle", "begin": [int(x) for x in begin.split(',')], "side": int(side)}

        elif type == 'square':
            while True:
                begin = input('Введите координаты левой нижней вершины в формате: x,y ---> ')
                if not re.match(r'[0-9]+,[0-9]+', begin):
                    continue
                side = input('Введите длину стороны: ---> ')
                if not side.isnumeric():
                    continue
                else:
                    break
            return {"type": "square", "begin": [int(x) for x in begin.split(',')], "side": int(side)}

        elif type == 'rectangle':
            while True:
                begin = input('Введите координаты левой нижней вершины в формате: x,y ---> ')
                if not re.match(r'[0-9]+,[0-9]+', begin):
                    continue
                diagonal_point = input('Введите координаты диагонально противоположной вершины в формате: x,y ---> ')
                if not re.match(r'[0-9]+,[0-9]+', diagonal_point):
                    continue
                else:
                    break
            begin = [int(x) for x in begin.split(',')]
            diagonal_point = [int(x) for x in diagonal_point.split(',')]
            return {"type": "rectangle", "begin": begin, "diagonal_point": diagonal_point}

        elif type == 'circle':
            while True:
                begin = input('Введите координаты центра в формате: x,y ---> ')
                if not re.match(r'[0-9]+,[0-9]+', begin):
                    continue
                radius = input('Введите радиус: ---> ')
                if not radius.isnumeric():
                    continue
                else:
                    break
            return {"type": "circle", "begin": [int(x) for x in begin.split(',')], "radius": int(radius)}

    def draw(self, type, begin, side = 100, diagonal_point = [0, 0], radius = 100, group=False):
        if type == 'triangle':
            self._goto(begin)
            t.forward(side)
            x = begin[0]+(side/2)
            y = round(begin[1]+0.866025*side)
            t.goto(x, y)
            t.goto(*begin)
            if not group:
                t.exitonclick()

        elif type == 'square':
            self._goto(begin)
            for _ in range(4):
                t.forward(side)
                t.left(90)
            if not group:
                t.exitonclick()

        elif type == 'rectangle':
            self._goto(begin)
            for _ in range(2):
                t.forward(diagonal_point[0])
                t.left(90)
                t.forward(diagonal_point[1])
                t.left(90)
            if not group:
                t.exitonclick()

        elif type == 'circle':
            t.up()
            t.goto(*begin)
            t.forward(radius)
            t.down()
            t.left(90)
            t.circle(radius)
            if not group:
                t.exitonclick()


def open_file():
    global file
    while True:
        file = input('Введите полный путь к файлу. Пример: /home/user/file.txt --->  ')
        if os.path.isfile(file):
            break
    try:
        content = json.load(open(file))
    except ValueError:
        print("Неверный синтаксис файла!")
        content = None
    return content


def is_valid_json(data):
    data = json.dumps(data)
    try:
        json.loads(data)
    except (ValueError, KeyError, TypeError):
        return False
    return True


if __name__ == '__main__':
    figure = Figure()
    print(wellcome_msg)

    while True:
        resp = input('--->  ')

        if resp == '0':
            print('Пока!')
            exit()

        # Рисуем фигуры
        elif resp == '1':
            print(fig_msg)
            fig = input('--->  ')

            # Вводим и рисуем треугольник
            if fig == '1':
                f = figure.get('triangle')
                figure.draw(**f)
                print(wellcome_msg)

            # Вводим и рисуем квадрат
            if fig == '2':
                f = figure.get('square')
                figure.draw(**f)
                print(wellcome_msg)

            # Вводим и рисуем прямоугольник
            if fig == '3':
                f = figure.get('rectangle')
                figure.draw(**f)
                print(wellcome_msg)

            # Вводим и рисуем окружность
            if fig == '4':
                f = figure.get('circle')
                figure.draw(**f)
                print(wellcome_msg)

            # Возврат в главное меню
            if fig == 0:
                print(wellcome_msg)
                continue

        # Если данные читаются из файла
        elif resp == '2':
            content = open_file()

            if content:
                for f in content:
                    figure.draw(group=True, **f)
                else:
                    t.exitonclick()
            print(wellcome_msg)

        # Если файл открывается для редактирования
        elif resp == '3':
            content = open_file()
            print("Содержимое файла %s: \n %s" % (file, content))
            while True:
                content = input("Введите новое содержимое файла: ---> ")
                if is_valid_json(content):
                    break
                else:
                    continue
            content = content.replace("'", '"')
            decoded = json.loads(content)
            with open(file, 'w') as f:
                json.dump(decoded, f, sort_keys=True, indent=4)
            print(wellcome_msg)

        # Создание файла с фигурами
        elif resp == '4':
            figs = []
            while True:
                print(add_fig_msg)
                print('Сейчас добавленно фигур(а):  %s' % len(figs))
                fig = input('Введите номер фигуры: ---> ')

                # Треугольник
                if fig == '1':
                    f = figure.get('triangle')
                    figs.append(f)
                    continue

                # Квадрат
                if fig == '2':
                    f = figure.get('square')
                    figs.append(f)
                    continue

                # Прямоугольник
                if fig == '3':
                    f = figure.get('rectangle')
                    figs.append(f)
                    continue

                # Окружность
                if fig == '4':
                    f = figure.get('circle')
                    figs.append(f)
                    continue

                # Запись в файл
                if fig == '9':
                    filename = input('Введите имя файла. Например: figure.json : ---> ')
                    with open(filename, 'w') as outfile:
                        json.dump(figs, outfile, sort_keys=True, indent=4)
                    print(wellcome_msg)
                    break

                # В главное меню
                if fig == '0':
                    print(wellcome_msg)
                    break

        else:
            print("Неверное значение. Повторите еще раз.")
