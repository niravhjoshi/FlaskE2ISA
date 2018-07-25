from flask_restful import reqparse, fields, marshal, Resource
import json
from flask import request
from flask_login import current_user, login_required
from app.models.Person_model import Persons, PersonSchema
from datetime import datetime
from app import db

persons_schema = PersonSchema(many=True)
person_schema = PersonSchema()


class PersonRes(Resource):
# This is  method for all persons
    @staticmethod
    @login_required
    def get():
        persons = Persons.query.filter_by(u_id=current_user.id)
        persons = persons_schema.dump(persons).data
        return {'status': 'success', 'data': persons}, 200

# This is new records creation Persons
    @staticmethod
    @login_required
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = person_schema.load(json_data)
        print data
        if errors:
            return errors, 422
        person = Persons.query.filter_by(u_id=current_user.id, per_name=data['per_name'],
                                         per_sex=data['per_sex'], per_bdate=data['per_bdate']).first()
        if person:
            return {'message': 'Person name already exists'}, 400
        newperson = Persons(u_id=current_user.id, per_name=data['per_name'], per_sex=data['per_sex'],
                            per_bdate=data['per_bdate'])
        try:
            db.session.add(newperson)
            db.session.commit()
            result = person_schema.dump(newperson).data
            return {"status": 'success', 'data': result}, 201
        except:
            return {'message': 'An error occured while creating Person'}, 500

# This is update method for Persons
    @staticmethod
    @login_required
    def put():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = person_schema.load(json_data)
        if errors:
            return errors, 422
        print json_data['id']
        person = Persons.query.filter_by(u_id=current_user.id, id=json_data['id']).first()
        if not person:
            return {'message': 'Person does not exist'}, 400
        try:
            person.per_name = data['per_name'],
            person.per_sex = data['per_sex'],
            person.per_bdate = data['per_bdate']
            db.session.commit()
            result = person_schema.dump(person).data
            print result
            return {"status": 'success', 'data': result}, 201
        except:
            return {'message': 'An error occured while updating Person'}, 500

#This is delete method for Persons
    @staticmethod
    @login_required
    def delete():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = person_schema.load(json_data)
        if errors:
            return errors, 422
        print data
        print json_data
        person = Persons.query.filter_by(u_id=current_user.id, id=json_data['id']).first()
        if person:
            try:
                persondel = Persons.query.filter_by(id=json_data['id'], u_id=current_user.id).delete()
                print persondel
                result = person_schema.dump(persondel).data
                db.session.commit()
                return {"status": 'success deleted', 'data': json_data['id'],'result':result}, 200
            except:
                return {'message': 'An error occured while Deleting Person'}, 500

#This is class for return single values for person.

class SinglePersonRes(Resource):
    @classmethod
    @login_required
    def get(cls,idx):
        person = Persons.query.filter_by(u_id=current_user.id, id=idx).first()
        if person:
            person = person_schema.dump(person).data
            return {'status': 'success', 'data': person}, 200
        return {'error': 'person  does not exist'}

