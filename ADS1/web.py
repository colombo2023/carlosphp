from bottle import route, run, template


@route('/hello/<name>')
def index(name):
    return template('<b>Oi {{a}}</b>!', a=name)

@route('/ex1/<m:>')
def ex1_route(m):

    

run(host='localhost', port=8081, reloader=True)
