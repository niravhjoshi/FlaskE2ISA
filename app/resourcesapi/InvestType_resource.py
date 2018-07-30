from flask_restplus  import  Resource
import json
from flask import request
from flask_login import current_user, login_required
from app.models.Investtype_model import InvType, InvestTypeSchema
from datetime import datetime
from app import db

invtypes_schema = InvestTypeSchema(many=True)
invtype_schema = InvestTypeSchema()

class InvestTypeRes(Resource):
    # This is  method for all ExpTypes
    @classmethod
    @login_required
    def get(cls):
        invtypes = InvType.query.filter_by(u_id=current_user.id)
        invtypes = invtypes_schema.dump(invtypes).data
        return {'status': 'success', 'data': invtypes}, 200

    # This is new records creation Persons
    @classmethod
    @login_required
    def post(cls):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = invtype_schema.load(json_data)
        print data
        if errors:
            return errors, 422
        invtype = InvType.query.filter_by(u_id=current_user.id,InvType_name=data['InvType_name']).first()
        if invtype:
            return {'message': 'Investment Type name already exists'}, 400
        newinvtype = InvType(u_id=current_user.id, InvType_name=data['InvType_name'])
        try:
            db.session.add(newinvtype)
            db.session.commit()
            result = invtype_schema.dump(newinvtype).data
            return {"status": 'success', 'data': result}, 201
        except:
            return {'message': 'An error occurred while creating Investment Type'}, 500

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
            return {'message': 'InvestmentType does not exist or there must be some expense entry created with it and it still prensent in database'}, 400
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
                return {'message': 'An error occured while Deleting Investment Type it might hold records in Investment.'}, 500

    # This is class for return single values for person.


class SingleInvestTypeRes(Resource):
    @classmethod
    @login_required
    def get(cls, idx):
        invtype = InvType.query.filter_by(u_id=current_user.id, id=idx).first()
        if invtype:
            exptype = invtype_schema.dump(invtype).data
            return {'status': 'success', 'data': exptype}, 200
        return {'error': 'Expense Type  does not exist'}

