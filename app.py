# CREATING A FLASK-RESTFULL APP

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Itemlist
from resources.store import Store, StoreList


app = Flask(__name__)
# SQLALCHEMY also work on PostgresSQL and NOSQL with only changing this setting
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False
app.secret_key = 'gerdin'
api = Api(app)



# JWT creates a new endpoint (= /auth), JWT gets the username and password
# and sends it to security file. If succesful the auth endpoint returns the
# the JWT token. In following request the JWT token (payload) is used to identify the
# right user via identity function
jwt = JWT(app, authenticate, identity)

api.add_resource(Item,'/item/<string:name>') #htatp://127.0.0.1:5000/student/Rolf
api.add_resource(Itemlist,'/items') #htatp://127.0.0.1:5000/student/Rolf
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

# prevents the app is runned if app.py is imported
# if we run a file Python assigns the name __main__ to this file
# so if it is not main, it means the file is imported
if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
