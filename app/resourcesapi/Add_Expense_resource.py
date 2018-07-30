from flask_restplus  import  Resource
import json
import sys, os, logging, time, datetime, json, uuid, requests, ast
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
from flask import request
from flask_login import current_user, login_required
from app.models.Expense_model import Expenses, ExpensesSchema
from datetime import datetime
from app import db

expenses_schema = ExpensesSchema(many=True)
expense_schema = ExpensesSchema()


class ExpenseRes(Resource):
    # This is  method for all ExpTypes
    @classmethod
    @login_required
    def get(cls):
        exptypes = Expenses.query.filter_by(U_id=current_user.id)
        exptypes = expenses_schema.dump(exptypes).data
        return {'status': 'success', 'data': exptypes}, 200

    # This is new records creation Persons
    @classmethod
    def post(cls):
        print "************DEBUG 1 ***********"
        RequestValues = request.values
        print RequestValues
        print "************DEBUG 2 ***********"
        RequestForm = request.form
        print RequestForm
        print "************DEBUG 2-1 ***********"
        so = RequestForm
        json_of_metadatas = so.to_dict(flat=False)
        print json_of_metadatas
        print "************DEBUG 2-2 ***********"
        MetdatasFromJSON = json_of_metadatas['jsondata']
        print MetdatasFromJSON
        print "************DEBUG 2-3 ***********"
        MetdatasFromJSON0 = MetdatasFromJSON[0]
        print MetdatasFromJSON0
        print "************DEBUG 3-5 ***********"
        strMetdatasFromJSON0 = str(MetdatasFromJSON0)
        MetdatasDICT = ast.literal_eval(strMetdatasFromJSON0)
        print MetdatasDICT
        print "************DEBUG 3-5 ***********"
        for key in MetdatasDICT:
            print "key: %s , value: %s" % (key, MetdatasDICT[key])
        print "************DEBUG 4 ***********"
        f = request.files['filedata']
        f.save(secure_filename(f.filename))
        print "FILE SAVED LOCALY"
        return 'JSON of customer posted'
'''
        posted_file = str(request.files['filedata'].read())
        posted_data = json.load(request.files['jsondata'])
        print posted_file
       #print posted_data
        return '{}\n{}\n'.format(posted_file,posted_data)




        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = expense_schema.load(json_data)
        print data
        if errors:
            return errors, 422
        expensetype = Expenses.query.filter_by(per_id = data['per_id'],
                                               U_id=current_user.id,
                                               Exp_per_name=data['Exp_per_name'],
                                               Exp_type_name = data['Exp_type_name'],
                                               Exp_amt=data['Exp_amt'],
                                               Exp_date=data['Exp_date']
                                               ).first()
        if expensetype:
            return {'message': 'Expense name already exists'}, 400
        newexpensetype = Expenses(u_id=current_user.id,
                             Exp_per_name=data['Exp_per_name'],
                             Exp_type_name=data['Exp_type_name'],
                             Exp_img = request.json['binary'],
                             Exp_FileName= request.json['file_name'],
                             Exp_amt=data['Exp_amt'],
                             Exp_date=data['Exp_date'],
                             Exp_comm= data['Exp_comm']
                             )

        try:
            db.session.add(newexpensetype)
            db.session.commit()
            result = expense_schema.dump(newexpensetype).data
            return {"status": 'success', 'data': result}, 201
        except:
            return {'message': 'An error occurred while creating Investment Type'}, 500
'''

'''
    # This is update method for Persons
    @classmethod
    @login_required
    def put(cls):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = invtype_schema.load(json_data)
        if errors:
            return errors, 422
        print json_data['id']
        invtype = InvType.query.filter_by(u_id=current_user.id, id=json_data['id']).first()
        if not invtype:
            return {
                       'message': 'InvestmentType does not exist or there must be some expense entry created with it and it still prensent in database'}, 400
        try:
            invtype.InvType_name = data['InvType_name'],
            db.session.commit()
            result = invtype_schema.dump(invtype).data
            print result
            return {"status": 'success', 'data': result}, 201
        except:
            return {'message': 'An error occurred while updating Investment Type please'}, 500

    # This is delete method for Persons
    @staticmethod
    @login_required
    def delete():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = invtype_schema.load(json_data)
        if errors:
            return errors, 422
        print data
        print json_data
        invtype = InvType.query.filter_by(u_id=current_user.id, id=json_data['id']).first()
        if invtype:
            try:
                invtypedel = InvType.query.filter_by(id=json_data['id'], u_id=current_user.id).delete()
                print invtypedel
                result = invtype_schema.dump(invtypedel).data
                db.session.commit()
                return {"status": 'success deleted', 'data': json_data['id'], 'result': result}, 200
            except:
                return {
                           'message': 'An error occured while Deleting Investment Type it might hold records in Investment.'}, 500

    # This is class for return single values for person.
'''

class SingleExpenseRes(Resource):
    @classmethod
    @login_required
    def get(cls, idx):
        expensetype = Expenses.query.filter_by(u_id=current_user.id, id=idx).first()
        if expensetype:
            expensetype = expense_schema.dump(expensetype).data
            return {'status': 'success', 'data': expensetype}, 200
        return {'error': 'Expense   does not exist'}

