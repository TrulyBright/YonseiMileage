import ws

def setup_websockets(app):
    app.add_websocket_route(ws.get_mileage_data, "/get_mileage_data")
