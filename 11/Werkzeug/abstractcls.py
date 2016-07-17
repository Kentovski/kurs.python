from abc import ABCMeta, abstractmethod


class Unit:
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_attack(self):
        pass

    @abstractmethod
    def take_damage(self, attack_value):
        pass

    @abstractmethod
    def get_recharge(self):
        pass

    @abstractmethod
    def get_health(self):
        pass
