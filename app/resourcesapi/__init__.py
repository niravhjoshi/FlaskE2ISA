from flask import Blueprint
from flask_restful import Api
from app.resourcesapi.Hello import Hello

api_bp = Blueprint('apinew', __name__)
api = Api(api_bp)

# Route
api.add_resource(Hello, '/Hello')


