#!/usr/bin/env python3

'''
Хохлов Андрей

'''

import MySQLdb
import MySQLdb.cursors
import models


USER = 'root'
PASSWORD = 'your_pass'
DB = 'your_db'


def get_connection():
    connection = MySQLdb.connect(user=USER,
                                 passwd=PASSWORD,
                                 db=DB,
                                 cursorclass=MySQLdb.cursors.DictCursor)
    return connection


def migrate(model):
    table_name = model.__class__.__name__
    f = []
    for field in model:
        f.append('`{}` {}'.format(field, model[field].query()))
    query = 'CREATE TABLE IF NOT EXISTS `{}`({})'.format(table_name, ' , '.join(f))
    print('Выполняю запрос: ', query)
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
    finally:
        cursor.close()
        connection.close()


def insert(model, **kwargs):
    table_name = model.__class__.__name__
    fields = ', '.join(kwargs.keys())
    values = ', '.join("'{}'".format(v) for v in kwargs.values())
    query = "INSERT INTO %s(%s) VALUES (%s)" % (table_name, fields, values)
    print('Выполняю запрос: ', query)
    try:
        connection = get_connection()
        cursor = connection.cursor()
        return bool(cursor.execute(query))
    except Exception:
        return False
    finally:
        cursor.close()
        connection.commit()
        connection.close()


def select(model, **kwargs):
    table_name = model.__class__.__name__
    args = [arg.split('__') if '__' in arg else arg for arg in kwargs]
    a = []
    for arg in args:
        if type(arg) == str:
            a.append('`{}` = "{}"'.format(arg, kwargs[arg]))
        else:
            if arg[1] == 'gt':
                key = arg[0] + '__gt'
                a.append('`{}` > "{}"'.format(arg[0], kwargs[key]))
            if arg[1] == 'lt':
                key = arg[0] + '__lt'
                a.append('`{}` < "{}"'.format(arg[0], kwargs[key]))

    where = ' AND '.join(a)
    query = "SELECT * FROM `{}` WHERE {}".format(table_name, where)
    print('Выполняю запрос: ', query)
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()


def main():
    class Personal(models.Model):
        id = models.IntField(primary_key=True, autoincrement=True)
        lastname = models.CharField(max_length=15, unique=True)
        profession = models.CharField(max_length=20)
        age = models.IntField()

    personal = Personal()

    migrate(personal)
    insert(personal, lastname='Kovalsky', profession='engineer', age=36)
    insert(personal, lastname='Svarovsky', profession='designer', age=46)
    insert(personal, lastname='Shilin', profession='architect', age=54)
    insert(personal, lastname='Vikul', profession='manager', age=25)
    insert(personal, lastname='Sova', profession='engineer', age=32)
    insert(personal, lastname='Sohin', profession='accountant', age=45)
    insert(personal, lastname='Ivanov', profession='engineer', age=23)

    print('Результат запроса: ', select(personal, id=3))
    print('Результат запроса: ', select(personal, profession='engineer'))
    print('Результат запроса: ', select(personal, age__gt=40))
    print('Результат запроса: ', select(personal, id__lt=5, age__gt=40))


if __name__ == '__main__':
    main()
