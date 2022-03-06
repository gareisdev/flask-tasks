from importlib.resources import path
from flask import Flask
from flask_cors import CORS


def create_app():

    app = Flask(__name__)
    CORS(app)

    from tasks.tasks import tasks_bp
    from users.users import users_bp
    
    app.register_blueprint(tasks_bp)
    app.register_blueprint(users_bp)

    return app