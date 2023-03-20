from flask import Flask
from flask_app.main.routes import main

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_pyfile("config.py", silent=False)
    if test_config is not None:
        app.config.update(test_config)

    app.register_blueprint(main)
    
    return app