#!/usr/bin/env python3
'''
Хохлов Андрей

'''

import io
from contextlib import redirect_stdout

import battle
from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    armies = int(request.args.get('armies', 2))
    solders = int(request.args.get('solders', 1))
    vehicles = int(request.args.get('vehicles', 1))
    squads = int(request.args.get('squads', 1))
    f = io.StringIO()
    battlefield = battle.BattleField(*[battle.Army('random', *[battle.Squad(solders, vehicles) for _ in range(squads)]) for _ in range(armies)])
    with redirect_stdout(f):
        battlefield.start()
        result = f.getvalue()
    resp = Response(result, status=200, mimetype='plain/text')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == "__main__":
    app.run(debug=True)
