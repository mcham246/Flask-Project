from . import db
from .model import User

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
