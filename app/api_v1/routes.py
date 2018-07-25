from flask import request,jsonify, abort
from app import app,db
from flask_login import current_user
from app.api_v1 import bp
from flask import render_template,flash, redirect, url_for, request
from flask_login import current_user, login_user,logout_user,login_required
from app.models.ExpType_model import ExpType
from app.models.Person_model import Persons
from app.models.Investtype_model import InvType
from app.models.Eartype_model import EarType
from flask_restful import reqparse

from app.models.Earning_model import Earnings
from app.models.Investment_model import Investments
from app.models.Expense_model import Expenses
from app.models.Share_model import Shares
import  json


#################
#ExpenseType API#
#################
#Get API Call for getting expense Types for loged in user
@bp.route('/api/V1/get_all_ExpenseTypes',methods =['GET'])
@login_required
def get_all_ExpenseTypes():
    return  jsonify({'ExpTypes': ExpType.get_all_exptypes()}),200

# Post API Call for Expense Type for create new Expense Type.

@bp.route('/api/V1/get_singlExpType/<int:id>',methods =['GET'])
@login_required
def get_singlExpType(id):
    if ExpType.get_single_expType(id) == 'Sorry No records found with this ID':
        return jsonify("Sorry No records found with this ID"),404
    else:
        return jsonify(ExpType.get_single_expType(id)),200

#Insert Expense Type into Database
@bp.route('/api/V1/Insert_singlExpType',methods =['POST'])
@login_required
def Insert_singlExpType():
    if not request.json or not 'Expense_Type' in request.json:
        return "There is no Expense_Type passed in Json Payload",400

    reqexptype = {'Expense_Type': request.json['Expense_Type'] }
    print reqexptype['Expense_Type']
    ExpType.add_expense_type(reqexptype['Expense_Type'])
    return jsonify({'ExpType': reqexptype}), 201

#Delete Expense Type from database
@bp.route('/api/V1/Del_singlExpType/<int:id>',methods=['DELETE'])
@login_required
def Del_singlExpType(id):
    if ExpType.get_single_expType(id) == 'Sorry No records found with this ID':
        return jsonify("Sorry No records found with this ID can not perform delete"), 404
    else:
        return jsonify(ExpType.delete_expType(id),{'ID':id,'result': True})


#Update Expense Type from database
@bp.route('/api/V1/Update_singlExpType/<int:id>',methods=['PUT'])
@login_required
def Update_singlExpType(id):
    if not request.json or not 'Expense_Type' in request.json:
        return "There is no Expense_Type passed in Json Payload", 400
    else:
        reqexptype = {'Expense_Type': request.json['Expense_Type']}
        print reqexptype['Expense_Type']
        if ExpType.get_single_expType(id) == 'Sorry No records found with this ID':
            return jsonify("Sorry No records found with this ID"), 404
        else:
            ExpType.update_expType(id,reqexptype['Expense_Type'])
        return jsonify({'id': id},'Updated Sucess'), 200


#################
#Person API#
#################
'''
#Get API Call for getting Persons for loged in user
@bp.route('/api/V1/get_all_persons',methods =['GET'])
@login_required
def get_all_persons():
    return  jsonify({'Persons': Persons.get_all_persons()}),200


# Get API Call for get single  Persons for logged in user.
@bp.route('/api/V1/get_person/<int:id>',methods =['GET'])
@login_required
def get_single_person(id):
    if Persons.get_single_person(id) == 'Sorry No records found with this ID':
        return jsonify("Sorry No records found with this ID"),404
    else:
        return jsonify(Persons.get_single_person(id)),200

#POST Insert new person into database.
@bp.route('/api/V1/Insert_person',methods =['POST'])
@login_required
def Insert_person():
    if not request.json or not 'per_name' or not 'per_sex' or not 'per_bdate' in request.json:
        return "There is no Expense_Type passed in Json Payload",400

    reqexptype = {'Expense_Type': request.json['Expense_Type'] }
    print reqexptype['Expense_Type']
    ExpType.add_expense_type(reqexptype['Expense_Type'])
    return jsonify({'ExpType': reqexptype}), 201

#Delete Expense Type from database
@bp.route('/api/V1/Del_Person/<int:id>',methods=['DELETE'])
@login_required
def Del_singlExpType(id):
    if ExpType.get_single_expType(id) == 'Sorry No records found with this ID':
        return jsonify("Sorry No records found with this ID can not perform delete"), 404
    else:
        return jsonify(ExpType.delete_expType(id),{'ID':id,'result': True})


#Update Expense Type from database
@bp.route('/api/V1/Update_Person/<int:id>',methods=['PUT'])
@login_required
def Update_singlExpType(id):
    if not request.json or not 'Expense_Type' in request.json:
        return "There is no Expense_Type passed in Json Payload", 400
    else:
        reqexptype = {'Expense_Type': request.json['Expense_Type']}
        print reqexptype['Expense_Type']
        if ExpType.get_single_expType(id) == 'Sorry No records found with this ID':
            return jsonify("Sorry No records found with this ID"), 404
        else:
            ExpType.update_expType(id,reqexptype['Expense_Type'])
        return jsonify({'id': id},'Updated Sucess'), 200
'''


####################
#InvestmentType API#
####################



#################
#EarningType API#
#################


###################
#Earning Entry API#
###################


###################
#Expense Entry API#
###################


######################
#Investment Entry API#
######################


###################
#Shares Entry API##
###################

