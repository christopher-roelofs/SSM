import server_config
from bottle import route, run, template

config = server_config.ServerConfig()

@route('/config')
def index():
    return template('config',config=config)

run(host='localhost', port=8080)



