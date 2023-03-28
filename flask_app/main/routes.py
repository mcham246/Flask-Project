from flask import Blueprint, render_template
from ..data_manager.data_scraper import DataScraper
main = Blueprint("main", __name__)

@main.route('/')
def index():
    object = DataScraper()
    df = object.getOffensiveLeadersStats()
    return render_template('index.html')