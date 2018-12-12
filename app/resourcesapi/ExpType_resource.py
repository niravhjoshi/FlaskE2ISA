from flask_restplus  import  Resource
import json
from flask import request
from flask_login import current_user, login_required
from app.models.ExpType_model import ExpType, ExpTypeSchema
from datetime import datetime
from app import db

exptypes_schema = ExpTypeSchema(many=True)
exptype_schema = ExpTypeSchema()

class ExpTypeRes(Resource):
    # This is  method for all ExpTypes
    @classmethod
    @login_required
    def get(cls):
        exptypes = ExpType.query.filter_by(u_id=current_user.id)
        exptypes = exptypes_schema.dump(exptypes).data
        return {'status': 'success', 'data': exptypes}, 200

    # This is new records creation Persons
    @classmethod
    @login_required
    def post(cls):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = exptype_schema.load(json_data)
        print data
        if errors:
            return errors, 422
        exptype = ExpType.query.filter_by(u_id=current_user.id,ExpType_name=data['ExpType_name']).first()
        if exptype:
            return {'message': 'ExpenseType name already exists'}, 400
        newexptype = ExpType(u_id=current_user.id, ExpType_name=data['ExpType_name'])
        try:
            db.session.add(newexptype)
            db.session.commit()
            result = exptype_schema.dump(newexptype).data
            return {"status": 'success', 'data': result}, 201
        except:
            return {'message': 'An error occured while creating ExpenseType'}, 500

    # This is update method for Persons
    @classmethod
    @login_required
    def put(cls):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = exptype_schema.load(json_data)
        if errors:
            return errors, 422
        print json_data['id']
        exptype = ExpType.query.filter_by(u_id=current_user.id, id=json_data['id']).first()
        if not exptype:
            return {'message': 'ExpenseType does not exist or there must be some expense entry created with it and it still prensent in database'}, 400
        try:
            exptype.ExpType_name = data['ExpType_name'],
            db.session.commit()
            result = exptype_schema.dump(exptype).data
            print result
            return {"status": 'success', 'data': result}, 201
        except:
            return {'message': 'An error occurred while updating Expense Type please'}, 500

    # This is delete method for Persons
    @staticmethod
    @login_required
    def delete():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = exptype_schema.load(json_data)
        if errors:
            return errors, 422
        print data
        print json_data
        exptype = ExpType.query.filter_by(u_id=current_user.id, id=json_data['id']).first()
        if exptype:
            try:
                exptypedel = ExpType.query.filter_by(id=json_data['id'], u_id=current_user.id).delete()
                print exptypedel
                result = exptype_schema.dump(exptypedel).data
                db.session.commit()
                return {"status": 'success deleted', 'data': json_data['id'], 'result': result}, 200
            except:
                return {'message': 'An error occured while Deleting Expense Type it might hold records in Expense.'}, 500

    # This is class for return single values for person.


class SingleExpTypeRes(Resource):
    @classmethod
    @login_required
    def get(cls, idx):
        exptype = ExpType.query.filter_by(u_id=current_user.id, id=idx).first()
        if exptype:
            exptype = exptype_schema.dump(exptype).data
            return {'status': 'success', 'data': exptype}, 200
        return {'error': 'Expense Type  does not exist'}
