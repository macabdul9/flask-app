from flask_restful import Api
from app import flaskApp

from .Task import Task



restServer = Api(flaskApp)


restServer.add_resource(Task, '/api/task')