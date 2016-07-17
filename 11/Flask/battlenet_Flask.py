#!/usr/bin/env python3
'''
Хохлов Андрей

'''

import io
from contextlib import redirect_stdout

import battle
from flask import Flask, render_template, redirect, url_for, request, session
from flask.ext.session import Session

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        armies = request.args.get('armies', 2)
        solders = request.args.get('solders', 1)
        vehicles = request.args.get('vehicles', 1)
        squads = request.args.get('squads', 1)
        f = io.StringIO()
        battlefield = battle.BattleField(*[battle.Army('random', *[battle.Squad(solders, vehicles) for _ in range(squads)]) for _ in range(armies)])
        with redirect_stdout(f):
            battlefield.start()
        session['result'] = f.getvalue()
        return redirect(url_for('index'))
    return render_template('index.html', result=session.get('result', ''))


if __name__ == "__main__":
    app.run(debug=True)
