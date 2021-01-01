from sanic import Sanic
from sanic.websocket import WebSocketProtocol
from sanja import conf_app as sanja_conf_app
from jinja2 import FileSystemLoader

from routes import setup_routes
from routes_websocket import setup_websockets

app = Sanic("YonseiMileageInformation")

# setup
app.static("/static", "./static")
setup_routes(app)
setup_websockets(app)
sanja_conf_app(app, auto_reload=True, loader=FileSystemLoader("templates/"))

if __name__ == '__main__':
    app.run(host="localhost", port=8080, protocol=WebSocketProtocol)
