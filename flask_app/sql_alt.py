from . import db
from .model import User, Test, Team
from .data_manager.data_manager_teams import TeamsDataScraper

class Database:
    
    def sample(self):
        person1 = User(
            id = 1234,
            name = 'Matarr',
            age = 26,
            address = '24222 Bush Hill Road',
            phone = '888-888-8888',
            email = 'me@outlook.com'
        )

        person2 = User(
            id = 4567,
            name = 'Bob',
            age = 20,
            address = '6666 Fake Lane',
            phone = '202-303-4040',
            email = 'bob@notreal.com'
        )

        person3 = User(
            id = 7890,
            name = 'Sue',
            age = 21,
            address = "7777 Imposter Drive",
            phone = '777-101-8888',
            email = 'sue@notreal.com'
        )

        person4 = User(
            id = 1111,
            name = 'Jim',
            address = '9000 Cap Road',
            phone = '444-444-4444',
            email = 'jim@notreal.com'
        )

        db.session.add(person1)
        db.session.add(person2)
        db.session.add(person3)
        db.session.add(person4)

        # db.session.commit()
        # User.query.delete()

    def sample2(self):
        test = Test(
            id = 8888888888,
            name = 'Test'
        )

        db.session.add(test)

    def query_team(self, team):
        object = TeamsDataScraper()
        df = object.scrape(object.allTeams[team])
        for i in range(0, len(df)-1):
            player = Team(
                id = i,
                name = df['PLAYER'][i],
                pos = df['POS'][i],
                gp = df['GP'][i],
                gs = df['GS'][i],
                min = df['MIN'][i],
                pts = df['PTS'][i],
                Or = df['OR'][i],
                dr = df['DR'][i],
                reb = df['REB'][i],
                ast = df['AST'][i],
                stl = df['STL'][i],
                blk = df['BLK'][i],
                to = df['TO'][i],
                pf = df['PF'][i],
                ast_to = df['AST/TO'][i]
            )
            db.session.add(player)