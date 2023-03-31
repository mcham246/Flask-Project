from flask import Blueprint, render_template
from ..data_manager.data_scraper import DataScraper
from ..model import User
from flask_sqlalchemy import SQLAlchemy
from .. import db

main = Blueprint("main", __name__)

@main.route('/')
def index():
    object = DataScraper()
    df = object.getOffensiveLeadersStats()

    something = User(
        id = 1234,
        name = 'Matarr',
        age = 26,
        address = '24222 Bush Hill Road',
        phone = '888-888-8888',
        email = 'me@outlook.com'
    )

    # db.session.add(something)
    # db.session.commit()
    # User.query.delete()

    users = User.query.all()
    print(users)
    


    return render_template('index.html', users=users)

