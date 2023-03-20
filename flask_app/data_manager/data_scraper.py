import requests
from bs4 import BeautifulSoup as bs
dict = {}

  
class DataScraper():

    def getOffensiveLeadersStats():
        URL = "https://www.espn.com/nba/stats/player"
        r = requests.get(url = URL)
        soup = bs(r.text, "html.parser")
        soup.prettify()
        p = soup.find('tbody')
        p = soup.find_all('a', class_="AnchorLink")
        for td in p:
            if "data-player-uid" in str(td):
                name = (td.find(text=True))
                if name not in dict:
                    dict[name] = {
                        'PTS': 0,
                        'REB': 1
                    }
    
        soup.find("tbody")
        p = soup.find_all('td', class_='Table__TD')
        for tr in p:
            print(tr.text)

if __name__ == "__main__":
    object = DataScraper
    object.getOffensiveLeadersStats()
