import logging

from flask import request
from flask_restplus import Resource
from application.api.truck.business import create_trucker, delete_trucker, update_trucker
from application.api.truck.serializers import trucker, trucker_with_posts
from application.api.restplus import api
from application.database.models import Trucker, TruckType

log = logging.getLogger(__name__)

ns = api.namespace('truck/driver', description='Operations related to truckers')


@ns.route('/')
class TruckerCollection(Resource):

    @api.response(404, 'a database result was required but none was found.')
    @api.marshal_list_with(trucker)
    def get(self):
        """
        Returns list of truck truckers.
        """
        truckers = Trucker.query.all()
        return truckers
    
    @api.response(201, 'trucker successfully created.')
    @api.response(500, 'internal server error.')
    @api.expect(trucker)
    def post(self):
        """
        Creates a new truck trucker.
        """
        data = request.json
        resp = TruckType.query.filter(TruckType.id == data["truck_type"]).count()
        if resp == 0:
            return {'message': 'Value entered in truck_type is not valid .'}, 400

        create_trucker(data)
        return None, 201

@ns.route('/<int:id>')
@api.response(404, 'trucker not found.')
class TruckerItem(Resource):
    
    @api.marshal_with(trucker_with_posts)
    def get(self, id):
        """
        Returns a trucker by id.
        """
        return Trucker.query.filter(Trucker.id == id).one()

    @api.expect(trucker)
    @api.response(204, 'trucker successfully updated.')
    def put(self, id):
        """
        Updates a trucker.

        Use this method to change the payload of a trucker.

        * Send a JSON object with the new name in the request body.

        ```
        {
            "age": 0,
            "cnh": "New Value",
            "destiny": "New Value",
            "gender": 0,
            "id": 0,
            "name": "New Value",
            "origin": "New Value",
            "owner_truck": 0,
            "truck_type": 0,
            "truckload": 0
        }
        ```

        * Specify the ID of the trucker to modify in the request URL path.
        """
        data = request.json
        update_trucker(id, data)
        return None, 204

    @api.response(204, 'trucker successfully deleted.')
    def delete(self, id):
        """
        Deletes truck trucker.
        """
        delete_trucker(id)
        return None, 204
