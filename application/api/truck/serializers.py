from flask_restplus import fields
from application.api.restplus import api

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

trucker = api.model('Truck trucker', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a trucker'),
    'name': fields.String(required=True, description='Trucker name'),
    'age': fields.Integer(required=True, description='Trucker age'),
    'gender': fields.Integer(required=True, description='Trucker gender'),
    'cnh': fields.String(required=True, description='Trucker CNH'),
    'truckload': fields.Integer(required=True, description='Trucker truckload'),
    'owner_truck': fields.Integer(required=True, description='Is owner truck'),
    'truck_type': fields.Integer(required=True, description='Whats truck type'),
    'origin': fields.String(required=True, description='Origin geolocalization'),
    'destiny': fields.String(required=True, description='Destiny geolocalization'),
    'created_at': fields.DateTime,
})

truck_type = api.model('Truck Type', {
    'name': fields.String(required=True, description='Trucker name'),
    'truck_type': fields.Integer(required=True, description='Whats truck type'),
})

report = api.model('Truck report', {
    'day': fields.Integer(required=True, description='By Day'),
    'week': fields.Integer(required=True, description='By Week'),
    'mounth': fields.Integer(required=True, description='By Mounth'),
})


trucker_with_posts = api.inherit('Truck trucker with posts', trucker, {
})
