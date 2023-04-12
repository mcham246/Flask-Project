from . import db

class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120), index=True)

class Test(db.Model):
    __tablename__='Test'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)





    