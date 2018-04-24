from flask import Blueprint

bp = Blueprint('addEPES',__name__)

from app.addEPES import routes