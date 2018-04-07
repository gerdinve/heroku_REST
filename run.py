from app import app
from db import db

db.init_app(app)

@app.before_first_request # this method is runned before the first request into this app
def create_tables():
    db.create_all()
