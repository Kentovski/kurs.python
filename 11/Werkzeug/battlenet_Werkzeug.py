#!/usr/bin/env python3
'''
Хохлов Андрей

'''

import io
from contextlib import redirect_stdout

import battle
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jinja2 import Environment, FileSystemLoader
from werkzeug.utils import redirect

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('index.html')
result = ''


@Request.application
def application(request):
    if request.method == 'POST':
        armies = request.args.get('armies', 2)
        solders = request.args.get('solders', 1)
        vehicles = request.args.get('vehicles', 1)
        squads = request.args.get('squads', 1)
        f = io.StringIO()
        battlefield = battle.BattleField(*[battle.Army('random', *[battle.Squad(solders, vehicles) for _ in range(squads)]) for _ in range(armies)])
        with redirect_stdout(f):
            battlefield.start()
        global result
        result = f.getvalue()
        return redirect('/')
    return Response(template.render(result=result), mimetype='text/html')


if __name__ == '__main__':
    run_simple('127.0.0.1', 5000, application, use_debugger=True, use_reloader=True)
