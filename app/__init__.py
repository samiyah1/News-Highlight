from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options




# Initializing application
app = Flask(__name__,instance_relative_config = True)

def create_app(config_name):
    app = Flask(__name__)
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    # Initializing Flask Extension
    bootstrap = Bootstrap(app) 
    
    # Will add the articles
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
     # Setting up configurations
    from .request import configure_request
    configure_request(app)

    return app 
