#!/usr/bin/env python3
'''
Хохлов Андрей
'''

import time
import random
import statistics

from abstractcls import Unit
from utils import last_hero, coroutine


class Vehicles(Unit):

    def __init__(self):
        self.operators = [Solder() for _ in range(1, random.randint(2, 4))]
        self.__health = 100
        self.__recharge = random.randint(1000, 2000)

    def get_health(self):
        if self.__health > 0 and any(bool(op.get_health() > 0) for op in self.operators):
            return statistics.mean(op.get_health() for op in self.operators) + self.__health
        else:
            return 0

    def do_attack(self):
        if self.__health > 0 and any(bool(op.get_health() > 0) for op in self.operators):
            attack_value = 0.5 * (1 + self.__health / 100) * statistics.mean(op.do_attack() for op in self.operators)
            return attack_value
        else:
            return 0

    def take_damage(self, attack_value):
        damage = abs(attack_value - (0.1 + sum(op.experience / 100 for op in self.operators)))
        self.__health -= 0.6 * damage
        if len(self.operators) == 1:
            self.operators[0].take_damage(0.4 * damage)
        if len(self.operators) == 2:
            self.operators[0].take_damage(0.2 * damage)
            self.operators[1].take_damage(0.2 * damage)
        if len(self.operators) == 3:
            unlucky = random.randint(0, 2)
            self.operators[unlucky].take_damage(0.2 * damage)
            lucky = [0, 1, 2]
            lucky.remove(unlucky)
            for i in lucky:
                self.operators[i].take_damage(0.1 * damage)
        print('БТР %s получил урон %.2f его здоровье %.2f\n' % (repr(self)[29:39], attack_value, self.__health))

    def get_recharge(self):
        return self.__recharge

    @coroutine
    def __call__(self):
        while True:
            attack_value = yield self.do_attack()
            # time.sleep(self.__recharge / 1000)
            if attack_value is not None:
                self.take_damage(attack_value)
            if self.__health <= 0:
                return '------------------> БТР %s умер\n' % repr(self)[26:37]


class Solder():

    def __init__(self):
        self.__recharge = random.randint(100, 2000)
        self.experience = 0
        self.__health = 100

    def do_attack(self):
        if self.__health <= 0:
            return 0
        attack_value = 0.5 * (1 + self.get_health() / 100) * random.randint(50 + self.experience, 100) / 100
        if self.experience < 50:
            self.experience += 1
        return attack_value

    def take_damage(self, attack_value):
        self.__health -= abs(attack_value - (0.05 + self.experience / 100))
        print('Солдат %s получил урон %.2f его здоровье %.2f\n' % (repr(self)[26:37], attack_value, self.get_health()))

    def get_health(self):
        if self.__health > 0:
            return self.__health
        else:
            return 0

    def get_recharge(self):
        return self.__recharge

    @coroutine
    def __call__(self):
        while True:
            attack_value = yield self.do_attack()
            # time.sleep(self.__recharge / 1000)
            if attack_value is not None:
                self.take_damage(attack_value)
            if self.get_health() <= 0:
                return '------------------> Солдат %s умер\n' % repr(self)[26:37]


class Squad:

    def __init__(self, solders, vehicles):
        #assert (5 <= solders + vehicles <=10), 'Общее количество юнитов в отряде должно быть от 5 до 10'
        self.units = [Solder() for _ in range(solders)] + [Vehicles() for _ in range(vehicles)]

    def get_power(self):
        power = statistics.mean(u.do_attack() for u in self.units)
        print('Отряд ', self, ' атакует с силой', power)
        return power

    def take_damage(self, attack_value):
        print('Отряд ', self, ' получил урон ', attack_value)
        for u in self.units:
            u.take_damage(attack_value / len(self.units))

    def get_health(self):
        return sum(unit.get_health() for unit in self.units)

    def __getitem__(self, index):
        return self.units[index]

    def __len__(self):
        return len(self.units)


class Army:

    def __init__(self, strategy='random', *squads):
        #assert len(squads) < 2, 'Количество отрядов должно быть больше 2'
        self.squads = squads
        if strategy in ['random', 'weakest', 'strongest']:
            self.strategy = strategy
        else:
            raise TypeError("Неверный тип стратегии")

    def __getitem__(self, index):
        return self.squads[index]

    def __len__(self):
        return len(self.squads)


class BattleField:

    def __init__(self, *armies):
        #assert len(armies) < 2, 'Количество армий должно быть больше 2'
        self.armies = armies

    def start(self):
        print('{:^80}\n'.format(' ИСХОДНЫЕ ЮНИТЫ '))
        for army in self.armies:
            print('Армия: ', repr(army), '\n')
            for squads in army:
                print('\tОтряд: ', repr(squads), '\n')
                for unit in squads:
                    print('\t\tЮнит: ', repr(unit), unit.get_health(), '\n')
        print('\n\n{:^80}'.format(' НАЧАЛО СИМУЛЯЦИИ \n'))
        while last_hero(self.armies):
            try:
                for army in self.armies:
                    for squad in army:
                        for unit in squad:
                            enemies = list(self.armies[:])
                            enemies.remove(army)
                            enemy = random.choice(random.choice(random.choice(enemies)))
                            if unit.get_health() and enemy.get_health():
                                attack_value = next(enemy())
                                unit().send(attack_value)
                                print('Юнит %s атаковал %s с силой %.2f\n' % (repr(enemy)[10:], repr(unit)[10:], attack_value))
            except StopIteration as exp:
                print(exp.value)
                continue

        for army in self.armies:
            print('Армия: ', army, '\n')
            for squads in army:
                print('\tОтряд: ', repr(squads), '\n')
                for unit in squads:
                    print('\t\tЮнит: ', repr(unit), unit.get_health())

if __name__ == '__main__':
    army1 = Army('random', Squad(1, 1), Squad(1, 1))
    army2 = Army('random', Squad(1, 1), Squad(1, 1))
    battle = BattleField(army1, army2)
    battle.start()
