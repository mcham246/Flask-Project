import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


class DataScraper():
    def __init__(self):
        self.names = []
        self.position = []
        self.team = []
        self.df = pd.DataFrame(columns=['PLAYER', 'TEAM', 'POS', 'GP', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', 
                                   '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'REB', 'AST',
                                   'STL', 'BLK', 'TO', 'DD2', 'TD3'])        

    def setOffensiveLeadersStats(self):
        # Finding the player names
        URL = "https://www.espn.com/nba/stats/player"
        r = requests.get(url = URL)
        soup = bs(r.text, "html.parser")
        soup.prettify()
        p = soup.find('tbody')
        p = soup.find_all('a', class_="AnchorLink")
        for td in p:
            if "data-player-uid" in str(td):
                name = (td.find(text=True))
                if name not in self.names:
                    self.names.append(name)
        # stored in 'self.names' list

        # Find the team the corresponding player plays for
        soup.find("tbody")
        p = soup.find_all('td')
        for tr in p:
            # print(tr.text)
            for name in self.names:
                if name in tr.text:
                    self.team.append(tr.text[len(name):])
        # stored in 'self.team'

        # Finding the player position
        soup.find("tbody")
        p = soup.find_all('div', class_='position')
        for tr in p:
            self.position.append(tr.text)
        # stored in "team" list

        # Finding the stats for the corresponding player
        soup.find("tbody")
        p = soup.find_all('td', class_='Table__TD')
        i = 0
        j = 0
        stats = []
        for tr in p:
            if 'position' not in str(tr) and 'AnchorLink' not in str(tr):
                if i >= 50:
                    # print(tr)
                    j += 1
                    stats.append(tr.text)
                if j == 19:
                    # print(stats)
                    # self.createDict(stats)
                    # print('---------------------------------------')
                    self.createDataFrame(stats)
                    stats = []
                    j = 0
                i += 1
    
    def getOffensiveLeadersStats(self):
        self.setOffensiveLeadersStats()
        print(self.df)
        return self.df

    # Save the dataframe to a csv file
    def save(self):
        self.df.to_csv(r'/Users/matarrcham/Documents/Flask-Project/data/test.csv', index=False)

    # utility method for finding player stats
    def createDict(self, stats):
        dict = {}
        dict[self.names.pop(0)] = {
            'TEAM': self.team.pop(0),
            'POS': self.position.pop(0),
            'GP': stats[0],
            'MIN': stats[1],
            'PTS': stats[2],
            'FGM': stats[3],
            'FGA': stats[4],
            'FG%': stats[5],
            '3PM': stats[6],
            '3PA': stats[7],
            '3P%': stats[8],
            'FTM': stats[9],
            'FTA': stats[10],
            'FT%': stats[11],
            'REB': stats[12],
            'AST': stats[13],
            'STL': stats[14],
            'BLK': stats[15],
            'TO': stats[16],
            'DD2': stats[17],
            'TD3': stats[18]
        }
        return dict

    def createDataFrame(self, stats):
        stats.insert(0, self.position.pop(0))
        stats.insert(0, self.team.pop(0))
        stats.insert(0, self.names.pop(0))
        self.df.loc[len(self.df)] = stats
    
if __name__ == "__main__":
    object = DataScraper()
    object.getOffensiveLeadersStats()
