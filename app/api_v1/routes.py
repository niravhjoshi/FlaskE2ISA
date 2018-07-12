from flask import request,jsonify, abort
from app import app,db
from flask_login import current_user
from app.api_v1 import bp
from flask import render_template,flash, redirect, url_for, request
from flask_login import current_user, login_user,logout_user,login_required
from app.models.ExpType_model import ExpType
import  json

#Get API Call for getting expense Types for loged in user
@bp.route('/api/V1/get_all_ExpenseTypes',methods =['GET'])
@login_required
def get_all_ExpenseTypes():
    return  jsonify({'ExpTypes': ExpType.get_all_exptypes()})

# Post API Call for Expense Type for create new Expense Type.

@bp.route('/api/V1/get_singlExpType/<int:id>',methods =['GET'])
@login_required
def get_singlExpType(id):
    return jsonify(ExpType.get_single_expType(id))
