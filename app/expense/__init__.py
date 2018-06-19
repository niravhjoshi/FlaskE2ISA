from flask import Blueprint

bp = Blueprint('expense',__name__)

from app.expense import routes