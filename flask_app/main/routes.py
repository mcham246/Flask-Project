from flask import Blueprint, render_template
from ..data_manager.data_scraper import DataScraper
from flaskext.mysql import MySQL
from ..model import Test

main = Blueprint("main", __name__)

@main.route('/')
def index():
    object = DataScraper()
    df = object.getOffensiveLeadersStats()

    something = Test()
    
    return render_template('index.html')