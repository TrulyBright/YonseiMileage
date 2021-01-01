import views

def setup_routes(app):
    app.add_route(views.index, "/")
