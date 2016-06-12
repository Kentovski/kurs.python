#!/usr/bin/env python3
'''
Хохлов Андрей

'''
import random
from collections import Counter, OrderedDict
from functools import reduce

import turtle as t


# Initial data
RADIUS = 90
input_string = 'hello world hello world nice to meet you'
mode = 'sectors'

# Initial Turtle settings
t.speed('fastest')


def draw_sector(angle, colour, x=0, y=0):
    if x == 0 and y == 0:
        t.forward(RADIUS)
        t.left(90)
    else:
        t.goto(x, y)

    t.begin_fill()
    t.fillcolor(colour)
    t.circle(RADIUS, angle)
    x, y = t.pos()
    t.goto(0, 0)
    t.end_fill()
    return (x, y)


def draw(input_string, mode='sectors'):
    if mode == 'sectors' and input_string != '':
        words_dict = Counter(input_string.split())
        words_dict = OrderedDict(sorted(words_dict.items(), key=lambda t: t[1], reverse=True))
        _num = reduce(lambda x, y: x+y, [item for _, item in words_dict.items()])
        angles = [((360 * words_dict[x]) // _num) for x in words_dict]
        colours = ["#%06x" % random.randint(0, 0xFFFFFF) for x in range(len(words_dict))]
        # Draw chart pie
        res = None
        for i, word in enumerate(words_dict):
            if res is None:
                res = draw_sector(angles[i], colours[i])
                continue
            res = draw_sector(angles[i], colours[i], *res)

        # Move  turtle to draw  chart legend
        t.pencolor('black')
        t.up()
        t.forward(150)
        t.right(90)
        t.forward(150)

        # Draw  legend
        for i, word in enumerate(words_dict):
            t.dot(10, colours[i])
            t.forward(20)
            t.pencolor(colours[i])
            t.right(90)
            t.forward(6)
            t.write('%s - %d time(s)' % (word, words_dict[word]), True, align="left")
            x, y = t.pos()
            t.goto(150, y-20)
            t.left(90)
    elif mode == 'rays' and input_string != '':
        words_dict = Counter(input_string.split())
        words_dict = OrderedDict(sorted(words_dict.items(), key=lambda t: t[1], reverse=True))
        angle = 360 // len(words_dict)
        colours = ["#%06x" % random.randint(0, 0xFFFFFF) for x in range(len(words_dict))]
        t.home()

        for i, word in enumerate(words_dict):
            t.pencolor(colours[i])
            for i in range(words_dict[word]):
                t.forward(RADIUS)
                t.dot(7)
            t.write(word, False, align="right")
            t.goto(0, 0)
            t.left(angle)
    else:
        print("Enter correct string and/or mode")


if __name__ == '__main__':
    draw(input_string, mode)
    t.exitonclick()
