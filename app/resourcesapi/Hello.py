from flask_restful import Resource


class Hello(Resource):
    @staticmethod
    def get():
        return {"message": "Hello, World!"}
    @staticmethod
    def post():
        return {"message": "Hello, World!"}