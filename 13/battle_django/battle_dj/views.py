import io
from contextlib import redirect_stdout

from django.shortcuts import render
from . import battle


def index(request):
    if request.method == 'POST':
        armies = int(request.POST.get('armies')) if request.POST.get('armies') else 2
        solders = int(request.POST.get('solders')) if request.POST.get('solders') else 1
        vehicles = int(request.POST.get('vehicles')) if request.POST.get('vehicles') else 1
        squads = int(request.POST.get('squads')) if request.POST.get('squads') else 1
        f = io.StringIO()
        battlefield = battle.BattleField(*[battle.Army('random', *[battle.Squad(solders, vehicles) for _ in range(squads)]) for _ in range(armies)])
        with redirect_stdout(f):
            battlefield.start()
        result = f.getvalue()
        return render(request, 'index.html', {'result': result})

    return render(request, 'index.html', {'result': 'Empty'})
