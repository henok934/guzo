from flask import Flask
def index():
    app = Flask(__name__)
    from .views import main
    app.register_blueprint(main)

    return app



