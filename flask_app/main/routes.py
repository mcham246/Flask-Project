from flask import Blueprint, render_template
from ..data_manager.data_scraper import DataScraper
from ..data_manager.data_manager_teams import TeamsDataScraper
from ..model import User, Test, Team
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


@main.route('/team_detail/<team>')
def team_detail(team):
    # print(team)
    object = TeamsDataScraper()
    # df = object.scrape(object.allTeams[team])
    # print(df)
    query = Database()
    query.query_team(team)
    team = Team.query
    return render_template('team_details.html', team=team)
