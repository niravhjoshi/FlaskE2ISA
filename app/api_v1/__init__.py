from flask import Blueprint

bp = Blueprint('apiV1',__name__)

from app.api_v1 import routes