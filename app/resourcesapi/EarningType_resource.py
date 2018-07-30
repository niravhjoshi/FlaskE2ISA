from flask_restplus  import  Resource
import json
from flask import request
from flask_login import current_user, login_required
from app.models.Eartype_model import EarType,EarTypeSchema
from datetime import datetime
from app import db

eartypes_schema = EarTypeSchema(many=True)
eartype_schema = EarTypeSchema()

class EarTypeRes(Resource):
    # This is  method for all ExpTypes
    @classmethod
    @login_required
    def get(cls):
        eartypes = EarType.query.filter_by(u_id=current_user.id)
        eartypes = eartypes_schema.dump(eartypes).data
        return {'status': 'success', 'data': eartypes}, 200

    # This is new records creation Persons
    @classmethod
    @login_required
    def post(cls):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = eartype_schema.load(json_data)
        print data
        if errors:
            return errors, 422
        eartype = EarType.query.filter_by(u_id=current_user.id,EarType_name=data['EarType_name']).first()
        if eartype:
            return {'message': 'EarningType name already exists'}, 400
        neweartype = EarType(u_id=current_user.id, EarType_name=data['EarType_name'])
        try:
            db.session.add(neweartype)
            db.session.commit()
            result = eartype_schema.dump(neweartype).data
            return {"status": 'success', 'data': result}, 201
        except:
            return {'message': 'An error occured while creating EarningType'}, 500

    # This is update method for Persons
    @classmethod
    @login_required
    def put(cls):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = eartype_schema.load(json_data)
        if errors:
            return errors, 422
        print json_data['id']
        eartype = EarType.query.filter_by(u_id=current_user.id, id=json_data['id']).first()
        if not eartype:
            return {'message': 'EarningType does not exist or there must be some expense entry created with it and it still prensent in database'}, 400
        try:
            eartype.ExpType_name = data['ExpType_name'],
            db.session.commit()
            result = eartype_schema.dump(eartype).data
            print result
            return {"status": 'success', 'data': result}, 201
        except:
            return {'message': 'An error occurred while updating Earning Type please contact admin'}, 500

    # This is delete method for Persons
    @staticmethod
    @login_required
    def delete():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = eartype_schema.load(json_data)
        if errors:
            return errors, 422
        print data
        print json_data
        eartype = EarType.query.filter_by(u_id=current_user.id, id=json_data['id']).first()
        if eartype:
            try:
                eartypedel = EarType.query.filter_by(id=json_data['id'], u_id=current_user.id).delete()
                print eartypedel
                result = eartype_schema.dump(eartypedel).data
                db.session.commit()
                return {"status": 'success deleted', 'data': json_data['id'], 'result': result}, 200
            except:
                return {'message': 'An error occured while Deleting Earning Type it might hold records in Earning.'}, 500

    # This is class for return single values for person.


class SingleExpTypeRes(Resource):
    @classmethod
    @login_required
    def get(cls, idx):
        eartype = EarType.query.filter_by(u_id=current_user.id, id=idx).first()
        if eartype:
            exptype = eartype_schema.dump(eartype).data
            return {'status': 'success', 'data': exptype}, 200
        return {'error': 'Earning Type  does not exist'}

