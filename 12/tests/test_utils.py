import os
from contextlib import redirect_stdout

from utils import last_hero
import battle


def test_last_hero():
    sq11 = battle.Squad(1, 1)
    sq12 = battle.Squad(1, 1)
    sq21 = battle.Squad(1, 1)
    sq22 = battle.Squad(1, 1)
    for _ in range(1000):
        with redirect_stdout(open(os.devnull, 'w')):
            sq12.take_damage(1)
            sq22.take_damage(1)
            sq22.take_damage(1)
    for _ in range(99):
        with redirect_stdout(open(os.devnull, 'w')):
            sq11.take_damage(1)

    army1 = battle.Army('random', sq11, sq12)
    army2 = battle.Army('random', sq21, sq22)

    assert last_hero([army1, army2])
