def last_hero(armies):
    true_list = []
    for army in armies:
        true_list.append(any(squad.get_health() for squad in army))
    if true_list.count(True) > 1:
        return True
    else:
        return False


def coroutine(f):
    def wrap(*args, **kwargs):
        gen = f(*args, **kwargs)
        gen.send(None)
        return gen
    return wrap
