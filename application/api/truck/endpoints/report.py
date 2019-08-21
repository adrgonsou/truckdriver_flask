import logging

from flask import request
from flask_restplus import Resource
from application.api.truck.business import create_trucker, delete_trucker, update_trucker
from application.api.truck.serializers import trucker, trucker_with_posts, report
from application.api.restplus import api
from application.database.models import Trucker

log = logging.getLogger(__name__)

ns = api.namespace('truck/report', description='By day, week and mouth')

@ns.route('/')
class ReportCollection(Resource):

    @api.response(404, 'a database result was required but none was found.')
    @api.marshal_list_with(report)
    def get(self):
        """
        Returns report by day, week and mouth.
        """
        
        truckers = Trucker.query.filter(Trucker.truckload == 0).all()
        return truckers
