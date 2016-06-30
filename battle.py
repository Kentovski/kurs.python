#!/usr/bin/env python3
'''
Хохлов Андрей
'''

import random
import statistics


class BattleField:
    def __init__(self, armies):
        self.armies = armies


class Army:
    def __init__(self, squads, strategy):
        self.squads = squads
        self.strategy = strategy


class Unit:

    def __init__(self):
        self.health = 100
        self.get_recharge()

    def do_attack(self):
        pass

    def take_damage(self):
        pass

    def get_recharge(self):
        self.recharge = random.randint(100, 2000)

    def get_health(self):
        return self.health


class Vehicles(Unit):

    def __init__(self, operators):
        self.operators = [Solder() for _ in range(random.randint(1, 3))]
        self.recharge = get_recharge()

    def get_health(self):
        return sum(op.get_health() for op in self.operators) + self.get_health()

    def do_attack(self):
        return 0.5 * (1 + self.health / 100) * statistics.mean(op.do_attack() for op in operators)

    def get_recharge(self):
        self.recharge = random.randint(1000, 2000)

    def take_damage(self, attack_value):
        self.health -= attack_value - (0.1 + sum(self.operators.experience / 100))


class Solder(Unit):

    def __init__(self):
        self.experience = 0

    def do_attack(self):
        attack = 0.5 * (1 + self.health/100) * random.randint(50 +
            self.experience, 100) / 100
        self.experience += random.randint(0, 50)
        return attack

    def take_damage(self, attack_value):
        self.health -= attack_value - (0.05 + self.experience / 100)


class Squad:

    def __init__(self, solders, vehicles):
        self.units = [Solder() for _ in range(1,solders)] + [Vehicles() for _ in range(1,vehicles)]

    def get_power(self):
        return sum(u.do_attack() for u in units)


    def take_damage(self, attack_value):
        self.health -= attack_value - sum(u.get_health() for u in units)
