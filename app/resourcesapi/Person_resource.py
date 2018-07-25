
from flask_restful import reqparse, fields, marshal, Resource
import json
from flask import request
from flask_login import current_user,login_required
from app.models.Person_model import Persons, PersonSchema
from datetime import datetime
from app import db

persons_schema = PersonSchema(many=True)
person_schema = PersonSchema()

'''
class SinglePerson(Resource):
    @login_required
    def get(self, _id):
        persons = Persons.query.filter_by(u_id=current_user.id, id=_id)
        if persons:
            persons = persons_schema.dump(persons).data
            return {'status': 'success', 'data': persons}, 200
        return {'error': 'person  does not exist'}

'''


class PersonRes(Resource):
    @staticmethod
    @login_required
    def get():
        persons = Persons.query.filter_by(u_id=current_user.id)
        persons = persons_schema.dump(persons).data
        return {'status': 'success', 'data': persons}, 200

    @staticmethod
    @login_required
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = person_schema.load(json_data)
        if errors:
            return errors, 422
        person = Persons.query.filter_by(u_id=current_user.id, per_name=data['per_name'],
                                         per_sex=data['per_sex'], per_bdate=data['per_bdate']).first()
        if person:
            return {'message': 'Person name already exists'}, 400
        newperson = Persons(
            per_name=json_data['per_name'],
            per_sex=json_data['per_sex'],
            per_bdate=json_data['per_bdate']
        )
        try:
            db.session.add(newperson)
            db.session.commit()
            result = person_schema.dump(newperson).data
            return {"status": 'success', 'data': result}, 201
        except:
            return {'message': 'An error occured while creating Person'}, 500

    @staticmethod
    @login_required
    def put():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = person_schema.load(json_data)
        if errors:
            return errors, 422
        person = Persons.query.filter_by(u_id=current_user.id, per_name=data['per_name'],
                                         per_sex=data['per_sex'], per_bdate=data['per_bdate']).first()
        if not person:
            return {'message': 'Person does not exist'}, 400
        try:
            person.per_name =data['per_name'],
            person.per_sex = data['per_sex'],
            person.per_bdate = data['per_bdate']
            db.session.commit()
            result = person_schema.dump(person).data
            return {"status": 'success', 'data': result}, 204
        except:
            return {'message': 'An error occured while updating Person'}, 500

    @staticmethod
    @login_required
    def delete():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = person_schema.load(json_data)
        if errors:
            return errors, 422
        person = Persons.query.filter_by(u_id=current_user.id, id=data['id']).first()
        if person:
            try:
                person = Persons.query.filter_by(id=data['id'],u_id= current_user.id).delete()
                db.session.commit()
                result = person_schema.dump(person).data
                return {"status": 'success', 'data': result}, 204
            except:
                return {'message': 'An error occured while Deleting Person'}, 500





