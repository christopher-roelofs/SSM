import server_config
from bottle import route, run, template



@route('/config')
def index():
    return template('config',config=server_config.config)

run(host='localhost', port=8080)



