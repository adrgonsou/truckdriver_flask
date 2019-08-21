import logging

from flask import request
from flask_restplus import Resource
from application.api.truck.business import create_trucker, delete_trucker, update_trucker
from application.api.truck.serializers import trucker, trucker_with_posts, truck_type
from application.api.restplus import api
from application.database.models import Trucker

log = logging.getLogger(__name__)

ns = api.namespace('geolocalization/truck-type', description='Operations related to geolocalization')


@ns.route('/')
class GeolocalizationCollection(Resource):

    @api.response(404, 'a database result was required but none was found.')
    @api.marshal_list_with(truck_type)
    def get(self):
        """
        Returns list of geolocalization by truck type.
        """

        #import pdb; pdb.set_trace()
    
        truckers = Trucker.query.filter(Trucker.owner_truck == 1).all()
        return truckers