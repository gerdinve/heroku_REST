# store uses in sqlit
# when users log call the auth endpoint we retrieve their credentials
# from the database and compare it to credentials they're sending in the request
# If it match the jwt token is send back

import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                    type=str,
                    required=True,
                    help = "This field cannot be empty"
    )
    parser.add_argument('password',
                    type=str,
                    required=True,
                    help = "This field cannot be empty"
    )

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        # ** data: for each of the keys in data, the key equals the value.
        #Because we use a parser we know both keys and values are present.
        #user = UserModel(data['username'], data['password'])
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created succesfully"}, 201
