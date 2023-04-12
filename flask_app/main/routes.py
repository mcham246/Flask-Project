from flask import Blueprint, render_template
from ..data_manager.data_scraper import DataScraper
from ..model import User
from flask_sqlalchemy import SQLAlchemy
from .. import db
from ..sql_alt import Database

main = Blueprint("main", __name__)

@main.route('/')
def index():
    
    object = Database()
    object.sample()
    users = User.query.all()


    


    return render_template('index_alt.html', users=users, title='Flask App')

