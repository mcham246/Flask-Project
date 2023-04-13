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


class Team(db.Model):
    __tablename__='Teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    pos = db.Column(db.String(64), index=True)
    gp = db.Column(db.String(64), index=True)
    gs = db.Column(db.String(64), index=True)
    min = db.Column(db.String(64), index=True)
    pts = db.Column(db.String(64), index=True)
    Or = db.Column(db.String(64), index=True)
    dr = db.Column(db.String(64), index=True)
    reb = db.Column(db.String(64), index=True)
    ast = db.Column(db.String(64), index=True)
    stl = db.Column(db.String(64), index=True)
    blk = db.Column(db.String(64), index=True)
    to = db.Column(db.String(64), index=True)
    pf = db.Column(db.String(64), index=True)
    ast_to = db.Column(db.String(64), index=True)



    