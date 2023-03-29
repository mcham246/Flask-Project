from flask import Flask
# import flask_mysql_connector as MySQL
from flaskext.mysql import MySQL

db = MySQL()

from flask_app.main.routes import main


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_pyfile("config.py", silent=False)
    if test_config is not None:
        app.config.update(test_config)

    db.init_app(app)
    # print(db)
    app.register_blueprint(main)
    return app