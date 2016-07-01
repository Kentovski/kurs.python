#!/usr/bin/env python3
'''
Хохлов Андрей

'''

import json


# Средняя температура в помещении в градусах цельсия
T_IN = 25

# Средняя наружная температура воздуха в градусах цельсия
T_OUT = -12

# Средняя температура грунта в градусах цельсия
T_GROUND = 8

# Количество отопительных дней
DAYS = 180

# Цена одной тонны угля, грн
COAL_PRICE = 3000


class Element:
    '''Конструкривный элемент, через который уходит тепло.
    Может принимать следующие типы: window, door, floor, wall, celling
    Параметр square - это площадь поверхности элемента, м2
    Параметр r - это общее термическое сопротивление ограждающей конструкции (м2*С)/Вт
    '''
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        assert self.type, 'Отсутствует тип конструкции'
        assert self.square, 'Отсутствует площадь поверхности конструкции'
        assert self.r, 'Отсутствует общее термическое сопротивление конструкции'

    def calc_elem_heat_losses(self):
        '''Теплопотери одного конструктивного элемента, Вт'''
        if self.type == 'floor':
            return ((T_IN - T_GROUND) * self.square) / self.r
        else:
            return ((T_IN - T_OUT) * self.square) / self.r

    def __repr__(self):
        return '{"type": "%s", "square": %s, "r": %s}' % (self.type, self.square, self.r)


class Room:

    def __init__(self,  *args):
        self.elements = args

    def calc_room_heat_losses(self):
        '''Потери тепла в комнате, Вт'''
        return sum(e.calc_elem_heat_losses() for e in self.elements)

    def __repr__(self):
        return '%s' % list(e for e in self.elements)


class House:

    def __init__(self, *args):
        self.rooms = args

    def calc_total_heat_losses(self):
        '''Потери тепла во всем доме, Вт'''
        return sum(r.calc_room_heat_losses() for r in self.rooms)

    def calc_anual_heating_price(self):
        '''
        На какую сумму необходимо закупить угля, чтобы обогреть всесь дом
        за отопительный период.
        '''
        # Сколько кг угля необходимо на сезон
        mass = (self.calc_total_heat_losses() * 24 * DAYS * 3600) / 29.3e6
        # Результат с поправкой на КПД твердотопливного котла 70 %
        return (mass * 1.3 / 1000) * COAL_PRICE

    def to_JSON(self):
        return str(list(r for r in self.rooms))

    @staticmethod
    def from_JSON(data):
        obj = json.loads(data)
        return House(*[Room(*[Element(**kwargs) for kwargs in room]) for room in obj])


if __name__ == '__main__':

    house = House(
            Room(
                    Element(type='window', square=1.25, r=0.42),
                    Element(type='window', square=1.25, r=0.42),
                    Element(type='wall', square=12.75, r=1.452),
                    Element(type='wall', square=10.75, r=1.452),
                    Element(type='wall', square=12, r=1.452),
                    Element(type='celling', square=10.5, r=3.84),
                    Element(type='floor', square=10.5, r=1.56),
                ),
            Room(
                    Element(type='window', square=1.25, r=0.42),
                    Element(type='window', square=1.25, r=0.42),
                    Element(type='door', square=2.1, r=0.36),
                    Element(type='wall', square=26.75, r=1.452),
                    Element(type='wall', square=18, r=1.452),
                    Element(type='wall', square=29.9, r=1.452),
                    Element(type='wall', square=26.75, r=1.452),
                    Element(type='celling', square=28, r=3.84),
                    Element(type='floor', square=28, r=1.56),
                )
        )

    #print('Дом теряет  %s Вт тепла за час.' % round(house.calc_total_heat_losses()))
    #print('На эту %s сумму необходимо закупить уголь.' % round(house.calc_anual_heating_price()))

    serialized_house = house.to_JSON()
    print('Объект House, сконвертированный в JSON: \n', serialized_house)

    house2 = House.from_JSON(serialized_house)
    print('Объект House, декодированный из JSON: \n', house2)
