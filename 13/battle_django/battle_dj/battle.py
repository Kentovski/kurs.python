#!/usr/bin/env python3

# Хохлов Андрей


import time
import random
import statistics

from .abstractcls import Unit
from .utils import last_hero, coroutine


class Vehicles(Unit):
    '''
    Vehicle class.

    :param (int) operators: Number of operators inside the vehicle. From 2 to 4.
    :param (int) __recharge: Random value from 1000 to 2000.
    :param (float) __health: Health of the vehicle.
    '''
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
        '''
        Calculate attack value of the vehicle.

        :returns:  Possible attack value of all units in the vehicle.
        '''
        if self.__health > 0 and any(bool(op.get_health() > 0) for op in self.operators):
            attack_value = 0.5 * (1 + self.__health / 100) * statistics.mean(op.do_attack() for op in self.operators)
            return attack_value
        else:
            return 0

    def take_damage(self, attack_value):
        '''
        Calculate health when the vehicle receive damage. The damage spreads of all solder in the vehicle.

        :param (float) attack_value: Value of damage to be taken.
        '''
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
        print('БТР %s получил урон %.2f его здоровье %.2f' % (repr(self)[29:39], attack_value, self.__health))

    def get_recharge(self):
        '''
        Get vehicle's recharge.

        :returns: Recharge value
        '''
        return self.__recharge

    @coroutine
    def __call__(self):
        '''
        Coroutine which receives damage and returns attack value of the vehicle.
        '''
        while True:
            attack_value = yield self.do_attack()
            # time.sleep(self.__recharge / 1000)
            if attack_value is not None:
                self.take_damage(attack_value)
            if self.__health <= 0:
                return '------------------> БТР %s умер' % repr(self)[26:37]


class Solder():
    '''
    Solder class.

    :param (int) experience: Each solder has experience which increments on attack. It must be from 0 to 50.
    :param (int) __recharge: Random value from 100 to 2000.
    :param (float) __health: Health of the solder.
    '''
    def __init__(self):
        self.__recharge = random.randint(100, 2000)
        self.experience = 0
        self.__health = 100

    def do_attack(self):
        '''
        Calculate attack value of the solder.

        :returns:  possible attack value
        '''
        if self.__health <= 0:
            return 0
        attack_value = 0.5 * (1 + self.get_health() / 100) * random.randint(50 + self.experience, 100) / 100
        if self.experience < 50:
            self.experience += 1
        return attack_value

    def take_damage(self, attack_value):
        '''
        Calculate health when the solder receive damage.

        :param (float) attack_value: Value of damage to be taken.
        '''
        self.__health -= abs(attack_value - (0.05 + self.experience / 100))
        print('Солдат %s получил урон %.2f его здоровье %.2f' % (repr(self)[26:37], attack_value, self.get_health()))

    def get_health(self):
        '''
        Get solder's health.
        '''
        if self.__health > 0:
            return self.__health
        else:
            return 0

    def get_recharge(self):
        '''
        Get solder's recharge.
        '''
        return self.__recharge

    @coroutine
    def __call__(self):
        '''
        Coroutine which receives damage and returns attack value of the solder.
        '''
        while True:
            attack_value = yield self.do_attack()
            # time.sleep(self.__recharge / 1000)
            if attack_value is not None:
                self.take_damage(attack_value)
            if self.get_health() <= 0:
                return '------------------> Солдат %s умер' % repr(self)[26:37]


class Squad:
    '''
    Squad consists of instances of class :class:`Solder` and :class:`Vehicles`

    :param (list) units: Number of solders and vehicles in the squad.
    '''
    def __init__(self, solders, vehicles):
        self.units = [Solder() for _ in range(solders)] + [Vehicles() for _ in range(vehicles)]

    def get_power(self):
        '''
        :returns:  Total atack value of all units in the squad.
        '''
        power = statistics.mean(u.do_attack() for u in self.units)
        print('Отряд ', self, ' атакует с силой', power)
        return power

    def take_damage(self, attack_value):
        '''
        Spreads damage among all units in the squad.

        :param (float) attack_value: Value of damage to be taken.
        '''
        print('Отряд ', self, ' получил урон ', attack_value)
        for u in self.units:
            u.take_damage(attack_value / len(self.units))

    def get_health(self):
        '''
        :returns:  Total health of all units in the squad.
        '''
        return sum(unit.get_health() for unit in self.units)

    def __getitem__(self, index):
        return self.units[index]

    def __len__(self):
        return len(self.units)


class Army:
    '''
    Army class.

    :param (list) squads: a list of squads, instances of class :class:`Squad`.
    :param (str) strategy: Main army strategy.
    '''
    def __init__(self, strategy='random', *squads):
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
    '''
    Main class of the battle simulator.

    :param armies: a list of armies, instances of class :class:`Army`. Number of armies must be greater than 2
    '''
    def __init__(self, *armies):
        self.armies = armies

    def start(self):
        '''
        Method which start battle simulation.
        '''
        print('{:^80}\n'.format(' ИСХОДНЫЕ ЮНИТЫ '))
        for army in self.armies:
            print('Армия: ', repr(army))
            for squads in army:
                print('\tОтряд: ', repr(squads))
                for unit in squads:
                    print('\t\tЮнит: ', repr(unit), unit.get_health())
        print('\n\n{:^80}'.format(' НАЧАЛО СИМУЛЯЦИИ '))
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
                                print('Юнит %s атаковал %s с силой %.2f' % (repr(enemy)[10:], repr(unit)[10:], attack_value))
            except StopIteration as exp:
                print(exp.value)
                continue

        for army in self.armies:
            print('Армия: ', army)
            for squads in army:
                print('\tОтряд: ', repr(squads))
                for unit in squads:
                    print('\t\tЮнит: ', repr(unit), unit.get_health())

if __name__ == '__main__':
    army1 = Army('random', Squad(1, 1), Squad(1, 1))
    army2 = Army('random', Squad(1, 1), Squad(1, 1))
    battle = BattleField(army1, army2)
    battle.start()
