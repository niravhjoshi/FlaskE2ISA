from flask import Blueprint
from flask_restful import Api
from app.resourcesapi.Hello import Hello
from app.resourcesapi.Person_resource import PersonRes,SinglePersonRes

api_bp = Blueprint('apiV2', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')
api.add_resource(PersonRes, '/PersonRes')
api.add_resource(SinglePersonRes, '/SinglePerRes/<string:idx>')
