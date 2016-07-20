import random
import os
from contextlib import redirect_stdout

import battle
import pytest


class TestSolder:

    def test_health(self):
        s = battle.Solder()
        for _ in range(400):
            s.take_damage(random.random())
        assert 0 <= s.get_health() <= 100

    def test_do_attack(self):
        s = battle.Solder()
        assert type(s.do_attack()) == float

    def test_take_damage_type(self):
        s = battle.Solder()
        s.take_damage('damage')
        with pytest.raises(TypeError):
            s.get_health()

    def test_get_health(self):
        s = battle.Solder()
        assert type(s.get_health()) == int or type(s.get_health()) == float


class TestVehicles:

    def test_health(self):
        v = battle.Vehicles()
        for _ in range(900):
            with redirect_stdout(open(os.devnull, 'w')):
                v.take_damage(random.random())
        assert 0 <= v.get_health() <= 100

    @pytest.mark.parametrize("damage", [0.45, 1, 0.0001, 0.1])
    def test_take_damage_type(self, damage):
        v = battle.Vehicles()
        v.take_damage(damage)
        assert type(v.get_health()) == int or type(v.get_health()) == float


class TestSquad:

    def test_health(self):
        sq = battle.Squad()
        for _ in range(900):
            with redirect_stdout(open(os.devnull, 'w')):
                sq.take_damage(random.random())
        assert 0 <= sq.get_health() <= 100

    @pytest.mark.parametrize("damage", [0.45, 1, 0.0001, 0.1])
    def test_take_damage_type(self, damage):
        sq = battle.Squad()
        sq.take_damage(damage)
        assert type(sq.get_health()) == int or type(sq.get_health()) == float


class TestArmy:

    @pytest.mark.parametrize("strategy", ['random', 'weakest', 'strongest', 'other'])
    def test_strategy(self, strategy):
        a = battle.Army(strategy, battle.Squad(1, 1), battle.Squad(1, 1))
        assert isinstance(a, battle.Army)
