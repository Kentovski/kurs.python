#!/usr/bin/env python3
'''
Хохлов Андрей

'''

import json

from abc import ABCMeta, abstractmethod


class VolumeMixin:
    ''' Примесь для вычисления объема'''
    @property
    def volume(self):
        return self.length * self.width * self.height


class WeightMixin:
    '''
     Примесь для вычисления веса тела.
    '''
    @property
    def weight(self):
        # 9.8 - это гравитационная постоянная
        return self.mass * 9.8


class Furniture(WeightMixin):

    def __init__(self, material, mass):
        # Возможные материалы: wood, glass, metal, wood-fibre
        if material not in ['wood', 'glass', 'metal', 'wood-fibre']:
            raise AttributeError("Неверный тип мебели")
        else:
            self.material = material
        self.mass = mass


class Table(Furniture):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super().__init__(self.material, self.mass)
        # Возможные типы: desktop, dinner, gaming, cook
        if self.type not in ['desktop', 'dinner', 'gaming', 'cook']:
            raise AttributeError("Неверный тип стола")

    def __repr__(self):
        return '{"%s": {"material": "%s", "mass": %s, "type": "%s"}}' % (self.__class__.__name__, self.material, self.mass, self.type)


class Chair(Furniture):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super().__init__(self.material, self.mass)
        # Возможные типы: folding, kitchen, solid
        if self.type not in ['folding', 'kitchen', 'solid']:
            raise AttributeError("Неверный тип стула")

    def __repr__(self):
        return '{"%s": {"material": "%s", "mass": %s, "type": "%s"}}' % (self.__class__.__name__, self.material, self.mass, self.type)

class Bed(Furniture):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super().__init__(self.material, self.mass)
        # Возможные типы: sofa,  double
        if self.type not in ['sofa', 'double']:
            raise AttributeError("Неверный тип кровати")

    def __repr__(self):
        return '{"%s": {"material": "%s", "mass": %s, "type": "%s"}}' % (self.__class__.__name__, self.material, self.mass, self.type)


class Refrigerator(Furniture):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super().__init__(self.material, self.mass)
        # Возможные типы: folding, kitchen, solid
        if self.energy_class not in ['A', 'B', 'C', 'D', 'E']:
            raise AttributeError("Неверный энерго класс холодильника")

    def __repr__(self):
        return '{"%s": {"material": "%s", "mass": %s, "energy_class": "%s"}}' % (self.__class__.__name__, self.material, self.mass, self.energy_class)


class Room(VolumeMixin):
    ''' Базовый класс комнаты '''
    def __init__(self, length, width, height, furniture):
        self.length = length
        self.width = width
        self.height = height
        # Список с экземплярами классов мебели
        self.furniture = furniture

    # Суммарный вес всей мебели в комнате
    @property
    def weight(self):
        return sum(f.weight for f in self.furniture)


class Kitchen(Room):
    name = "кухня"


class Bedroom(Room):
    name = "спальня"


class House(WeightMixin, VolumeMixin):
    # Какие-то дополнительные свойства
    properties = None

    def __init__(self, rooms, properties):
        self.rooms = rooms
        self.properties = properties

    @property
    def volume(self):
        return sum(room.volume for room in self.rooms)

    @property
    def weight(self):
        return sum(room.weight for room in self.rooms)


class Encoder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def load(self, data):
        """
        Загружает данные из строки и возвращает сконструированный объект
        :param data:
        :return: Получившийся объект
        """
        pass

    @abstractmethod
    def dump(self, obj):
        """
        ПОлучив объект - возвращает строку в каком-либо формате
        :param obj:
        :return:
        """
        pass


class JSONEncoder(Encoder):

    def __init__(self, obj=None, data=None):
        self.obj = obj
        self.data = data

    def load(self, data):
        rooms = []
        for room, room_params in data.items():
            if room != 'properties':
                if room == 'Bedroom':
                    p = []
                    for furniture in room_params['furniture']:
                        class_ = furniture.popitem()
                        p.append(type(class_[0], (Furniture, ), class_[1]))
                    rooms.append(Bedroom(room_params['length'], room_params['width'], room_params['height'], p))

                if room == 'Kitchen':
                    p = []
                    for furniture in room_params['furniture']:
                        class_ = furniture.popitem()
                        p.append(type(class_[0], (Furniture, ), class_[1]))
                    rooms.append(Kitchen(room_params['length'], room_params['width'], room_params['height'], p))

        return House(rooms, data['properties'])

    def dump(self, obj):
        res = {}
        for room in obj.rooms:
            res[room.__class__.__name__] = room.__dict__
            res["properties"] = house.properties
        return str(res).replace("'", '"')


if __name__ == '__main__':
    house = House([
        Kitchen(6, 7, 4, [
            Refrigerator(material='metal', mass=95, energy_class='B'),
            Table(material='wood', mass=30, type='dinner'),
            Chair(material='wood', mass=7, type='solid'),
            Chair(material='wood', mass=7, type='solid'),
            Chair(material='wood', mass=7, type='solid'),
            Chair(material='wood', mass=7, type='solid'),
            Bed(material='wood', mass=54, type='sofa')
        ]),
        Bedroom(5, 6, 4, [
            Chair(material='wood', mass=15, type='folding'),
            Table(material='wood-fibre', mass=18, type='desktop'),
            Table(material='glass', mass=27, type='gaming'),
            Bed(material='wood', mass=67, type='double'),
            Chair(material='metal', mass=12, type='kitchen'),
            Chair(material='wood', mass=7, type='solid')
        ])
    ], {"chimney": "no", "color": "grey", "fence": "yes"})
    j = JSONEncoder()
    r = j.dump(house)
    print('JSON сгенерированый через JSONEncoder \n', r)

    data = json.loads(r)
    pseudo_House = j.load(data)
    print('Объект pseudo_HouseJSON сгенерированый из JSONEncoder \n', pseudo_House.__dict__)
