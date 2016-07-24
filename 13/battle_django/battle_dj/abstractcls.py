from abc import ABCMeta, abstractmethod


class Unit:
    '''
    Abstract class Unit. The parent of all units.
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def do_attack(self):
        '''
        Abstract method to unit's attack.
        '''
        pass

    @abstractmethod
    def take_damage(self, attack_value):
        '''
        Abstract method to take damage.
        '''
        pass

    @abstractmethod
    def get_recharge(self):
        '''
        Abstract method of getting recharge.
        '''
        pass

    @abstractmethod
    def get_health(self):
        '''
        Abstract method of getting health.
        '''
        pass
