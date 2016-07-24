def last_hero(armies):
    '''
    :param armies: a list of armies. This is property of class :class:`BattleField`.
    :returns:  bool.

    Calculate the state of army where only one solder has left.
    It takes a list and returns True if there's only one solder in list of all armies.
    Otherwise returns False.

    '''
    true_list = []
    for army in armies:
        true_list.append(any(squad.get_health() for squad in army))
    if true_list.count(True) > 1:
        return True
    else:
        return False


def coroutine(f):
    '''

    :param f: a coroutine to initialise.
    :returns:  coroutine.

    Decorator to initialize coroutine.
    It make something like this:

    >>> def my_coroutine():
    >>>    ...
    >>> next(my_coroutine)

    '''
    def wrap(*args, **kwargs):
        gen = f(*args, **kwargs)
        gen.send(None)
        return gen
    return wrap


def fibgen(num):
    """
    Generates Fibonacci numbers

    :param num: how many numbers to generate
    :return: generator of first num Fibonacci numbers

    >>> list(fibgen(10))
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    if type(num) is not int:
        raise TypeError("type of num argument should be int")
    if num <= 0:
        return
    x1 = 0
    x2 = 1
    i = 1
    yield 1
    while i < num:
        i = i + 1
        res = x1 + x2
        x1 = x2
        x2 = res
        yield res