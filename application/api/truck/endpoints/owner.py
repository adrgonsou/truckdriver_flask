import logging

from flask import request
from flask_restplus import Resource
from application.api.truck.business import create_trucker, delete_trucker, update_trucker
from application.api.truck.serializers import trucker, trucker_with_posts
from application.api.restplus import api
from application.database.models import Trucker

log = logging.getLogger(__name__)

ns = api.namespace('truck/owner', description='Operations related to truckers Owners')


@ns.route('/')
class OwnerCollection(Resource):

    @api.response(404, 'a database result was required but none was found.')
    @api.marshal_list_with(trucker)
    def get(self):
        """
        Returns list of truck Owner.
        """
        truckers = Trucker.query.filter(Trucker.owner_truck == 1).all()
        return truckers
