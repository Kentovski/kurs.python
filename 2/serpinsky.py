#!/usr/bin/env python3
'''
Хохлов Андрей

'''
import turtle as t

# Initial cords
x1 = 0
y1 = 0
x2 = 400
y2 = 0
x3 = 200
y3 = 346
n = 5   # Number of iterations

# Initial settings
t.speed('fastest')


def draw(x1, y1, x2, y2, x3, y3, n):
    if n > 0:
        x12 = (x1 + x2) // 2
        y12 = (y1 + y2) // 2
        x23 = (x2 + x3) // 2
        y23 = (y2 + y3) // 2
        x31 = (x3 + x1) // 2
        y31 = (y3 + y1) // 2
        t.pu()
        t.goto(x31, y31)
        t.pd()
        t.goto(x12, y12)
        t.goto(x23, y23)
        t.goto(x31, y31)
        draw(x1, y1, x12, y12, x31, y31, n - 1)
        draw(x2, y2, x12, y12, x23, y23, n - 1)
        draw(x3, y3, x31, y31, x23, y23, n - 1)

if __name__ == '__main__':
    t.pu()
    t.goto(x1, y1)
    t.pd()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1, y1)
    draw(x1, y1, x2, y2, x3, y3, n)

    t.exitonclick()
