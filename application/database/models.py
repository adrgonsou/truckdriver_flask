# The examples in this file come from the Flask-SQLAlchemy documentation
# For more information take a look at:
# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#simple-relationships

from datetime import datetime

from application.database import db

class Trucker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    cnh = db.Column(db.String)
    truckload = db.Column(db.String)
    owner_truck = db.Column(db.Integer)
    truck_type = db.Column(db.Integer)
    origin = db.Column(db.String)
    destiny = db.Column(db.String)
    created_at = db.Column(db.Date)

    def __init__(self, name, age, gender,cnh, truckload, owner_truck, truck_type, origin, destiny, created_at=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.gender = gender
        self.cnh = cnh
        self.truckload = truckload
        self.owner_truck = owner_truck
        self.truck_type = truck_type
        self.origin = origin
        self.destiny = destiny
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Trucker %r>' % self.name, self.name, self.gender, self.cnh, self.truckload, self.owner_truck, self.truck_type, self.origin, self.destiny, self.created_at 

class TruckType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<TruckType %r>' % self.name 