from flask import Blueprint, render_template
from ..data_manager.data_scraper import DataScraper
from ..data_manager.data_manager_teams import TeamsDataScraper
from ..model import User, Test
from flask_sqlalchemy import SQLAlchemy
from .. import db
from ..sql_alt import Database

main = Blueprint("main", __name__)

@main.route('/')
def index():
    atlantic = []
    object = TeamsDataScraper()
    return render_template('index.html', atlantic=object.atlanticTeams.keys(), pacific=object.pacificTeams.keys(), 
                           central=object.centralTeams.keys(), southeast=object.southeastTeams.keys(), 
                           northwest=object.northwestTeams.keys(), southwest=object.southwestTeams.keys(), title='Flask App')

