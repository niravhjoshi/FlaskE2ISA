from flask import Blueprint

bp = Blueprint('earnings',__name__)

from app.earnings import routes