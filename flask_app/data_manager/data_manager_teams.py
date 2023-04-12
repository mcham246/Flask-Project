import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

class TeamsDataScraper:
    def __init__(self):
        self.atlanticTeams = {
            'Boston Celtics': 'https://www.espn.com/nba/team/stats/_/name/bos/boston-celtics',
            'Brooklyn Nets': 'https://www.espn.com/nba/team/stats/_/name/bkn/brooklyn-nets',
            'New York Knicks': 'https://www.espn.com/nba/team/stats/_/name/ny/new-york-knicks',
            'Philadelphia 76ers': 'https://www.espn.com/nba/team/stats/_/name/phi/philadelphia-76ers',
            'Toronto Raptors': 'https://www.espn.com/nba/team/stats/_/name/tor/toronto-raptors'
        }

        self.pacificTeams = {
            'Golden State Warriors': 'https://www.espn.com/nba/team/stats/_/name/gs/golden-state-warriors',
            'LA Clippers': 'https://www.espn.com/nba/team/stats/_/name/lac/la-clippers',
            'Los Angeles Lakers': 'https://www.espn.com/nba/team/stats/_/name/lal/los-angeles-lakers',
            'Phoenix Suns': 'https://www.espn.com/nba/team/stats/_/name/phx/phoenix-suns',
            'Sacramento Kings': 'https://www.espn.com/nba/team/stats/_/name/sac/sacramento-kings'
        }

        self.centralTeams = {
            'Chicago Bulls': 'https://www.espn.com/nba/team/stats/_/name/chi/chicago-bulls',
            'Cleveland Cavaliers': 'https://www.espn.com/nba/team/stats/_/name/cle/cleveland-cavaliers',
            'Detroit Pistons': 'https://www.espn.com/nba/team/stats/_/name/det/detroit-pistons',
            'Indiana Pacers': 'https://www.espn.com/nba/team/stats/_/name/ind/indiana-pacers',
            'Milwaukee Bucks': 'https://www.espn.com/nba/team/stats/_/name/mil/milwaukee-bucks'
        }

        self.southeastTeams = {
            'Atlanta Hawks': 'https://www.espn.com/nba/team/stats/_/name/atl/atlanta-hawks',
            'Charlotte Hornets': 'https://www.espn.com/nba/team/stats/_/name/cha/charlotte-hornets',
            'Miami Heat': 'https://www.espn.com/nba/team/stats/_/name/mia/miami-heat',
            'Orlando Magic': 'https://www.espn.com/nba/team/stats/_/name/orl/orlando-magic',
            'Washington Wizards': 'https://www.espn.com/nba/team/stats/_/name/wsh/washington-wizards'
        }

        self.northwestTeams = {
            'Denver Nuggets': 'https://www.espn.com/nba/team/stats/_/name/den/denver-nuggets',
            'Minnesota Timberwolves': 'https://www.espn.com/nba/team/stats/_/name/min/minnesota-timberwolves',
            'Oklahoma City Thunder': 'https://www.espn.com/nba/team/stats/_/name/okc/oklahoma-city-thunder',
            'Portland Trail Blazers': 'https://www.espn.com/nba/team/stats/_/name/por/portland-trail-blazers',
            'Utah Jazz': 'https://www.espn.com/nba/team/stats/_/name/utah/utah-jazz'

        }

        self.southwestTeams  = {
            'Dallas Mavericks': 'https://www.espn.com/nba/team/stats/_/name/dal/dallas-mavericks',
            'Houston Rockets': 'https://www.espn.com/nba/team/stats/_/name/hou/houston-rockets',
            'Memphis Grizzlies': 'https://www.espn.com/nba/team/stats/_/name/mem/memphis-grizzlies',
            'New Orleans Pelicans': 'https://www.espn.com/nba/team/stats/_/name/no/new-orleans-pelicans',
            'San Antonio Spurs': 'https://www.espn.com/nba/team/stats/_/name/sa/san-antonio-spurs'
        }

    def scrape(self, espnurl):
        # request configurations
        r = requests.get(url = espnurl)
        soup = bs(r.text, "html.parser")
        soup.prettify()

        # finding the people who have played this season for each team
        players = [] 
        p = soup.find('tbody')
        p = soup.find_all('a', class_="AnchorLink")
        count = 0
        for td in p:
           if td.text == 'GP':
               break
           if count >= 23:
                # print(str(count) + ': ' + td.text)
                players.append(td.text)
           count += 1
        # print(players)
        # print(len(players))

        # finding the position played by the players
        position = []
        p = soup.find_all('span', class_='font10') 
        count = 0
        for span in p:
            if count < len(players):
                # print(str(count) + ': ' + span.text)
                position.append(span.text)
            count +=1
        # print(len(position))

        # Finding the corresponding stats data for each player
        data = []
        p = soup.find_all('span', class_='') 
        count = 0
        line = 0
        tool = []
        numlines = 0
        for span in p:
            if count > len(players) and count <= (len(players) * 13) + len(players):
                # print(str(count) + ': ' + span.text)
                tool.append(span.text)
                line += 1

            if line == 13:
                # print('---------------------:' + str(numlines))
                data.append(tool)
                tool = []
                numlines += 1
                line = 0
            count +=1

        #create a dataframe out of data and return
        df = pd.DataFrame(columns=['PLAYER', 'POS','GP', 'GS', 'MIN', 'PTS', 'OR', 'DR', 'REB', 'AST', 'STL', 'BLK', 'TO', 'PF', 'AST/TO'])
        for i,p in enumerate(data):
            p.insert(0, position[i])
            p.insert(0, players[i])
            df.loc[len(df)] = p
        print(df)
        return df
    
    def getData(self):
        for teams in self.atlanticTeams:
            print('------------------' + teams + '------------------')
            self.scrape(self.atlanticTeams[teams])
        
        for teams in self.pacificTeams:
            print('------------------' + teams + '------------------')
            self.scrape(self.pacificTeams[teams])
        
        for teams in self.centralTeams:
            print('------------------' + teams + '------------------')
            self.scrape(self.centralTeams[teams])    
        
        for teams in self.southeastTeams:
            print('------------------' + teams + '------------------')
            self.scrape(self.southeastTeams[teams])
        
        for teams in self.northwestTeams:
            print('------------------' + teams + '------------------')
            self.scrape(self.northwestTeams[teams])
        
        for teams in self.southwestTeams:
            print('------------------' + teams + '------------------')
            self.scrape(self.southwestTeams[teams])

    
if __name__ == '__main__':
    object = TeamsDataScraper()
    object.getData()
