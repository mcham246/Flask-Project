from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask_app.main.routes import main
from flask_app import model

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_pyfile("config.py", silent=False)
    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app