from flask import Blueprint
main = Blueprint('main', __name__)
from .import views, error

def create_App(config_name)
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions 
    bootstrap.init_app(app)

    # Registering the Blueprint

    from.main import main as main Blueprint
    app.register_blueprint(main_print)

    return app