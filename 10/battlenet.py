import io
from wsgiref.simple_server import make_server
from cgi import parse_qs
from contextlib import redirect_stdout

import battle


def application(environ, start_response):

    with open('index.html', encoding='utf-8') as f:
        html = f.read()

    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size).decode(encoding='utf-8')
    d = parse_qs(request_body)

    armies = 2 if type (d.get('armies', 0)) == int else int(d.get('armies', 0).pop(0))
    solders = 1 if type (d.get('solders', 0)) == int else int(d.get('solders', 0).pop(0))
    vehicles = 1 if type (d.get('vehicles', 0)) == int else int(d.get('vehicles', 0).pop(0))
    squads =  1 if type (d.get('squads', 0)) == int else int(d.get('squads', 0).pop(0))

    if environ['REQUEST_METHOD'] == 'POST':
        f = io.StringIO()
        battlefield = battle.BattleField(*[battle.Army('random', *[battle.Squad(solders, vehicles) for _ in range(squads)]) for _ in range(armies)])
        with redirect_stdout(f):
            battlefield.start()
        response_body = html.format(result=f.getvalue())
    else:
        response_body = html.format(result='Пусто')

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes(response_body, 'utf-8')]


if __name__ == '__main__':
    httpd = make_server('localhost', 8051, application)
    httpd.serve_forever()
