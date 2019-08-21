from application.database import db
from application.database.models import Trucker

def create_trucker(data):
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    cnh = data.get('cnh')
    truckload = data.get('truckload')
    owner_truck = data.get('owner_truck')
    truck_type = data.get('truck_type')
    origin = data.get('origin')
    created_at = data.get('created_at')
    destiny = data.get('destiny')
    trucker = Trucker(name, age, gender, cnh, truckload, owner_truck, truck_type, origin, destiny, created_at)
    db.session.add(trucker)
    db.session.commit()


def update_trucker(trucker_id, data):
    trucker = Trucker.query.filter(Trucker.id == trucker_id).one()
    trucker.name = data.get('name')
    trucker.age = data.get('age')
    trucker.gender = data.get('gender')
    trucker.cnh = data.get('cnh')
    trucker.truckload = data.get('truckload')
    trucker.owner_truck = data.get('owner_truck')
    trucker.truck_type = data.get('truck_type')
    trucker.origin = data.get('origin')
    trucker.destiny = data.get('destiny')
    db.session.add(trucker)
    db.session.commit()


def delete_trucker(trucker_id):
    trucker = Trucker.query.filter(Trucker.id == trucker_id).one()
    db.session.delete(trucker)
    db.session.commit()
