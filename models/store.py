from db import db

# db Model indicates the class are things that are saved to and
# retrieved from the database, i.e. mapping between objects and database
class StoreModel(db.Model):
    # defining the mapped table and columnsand must be matched
    # with the object properties.
    __tablename__ = 'stores'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))

    # when we use dynamic self.items is not langer a list of items, but a query
    # builder that has the ability to look into the items table. This means untill
    # we call json method we are not lookig into the table. WIth no 'dynamic' for each store
    # we already load up all the belonging items
    # speed of creation of a store (faster by dynamic) vs speed of calling the JSON method (faster without lazy)
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    # convert item model to JSON representation
    def json(self):
        return {"name":self.name, "items": [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls,name):
        #quyering without connection info and convert the result to an object
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name = name LIMIT 1

    def save_to_db(self):
        # session is a collection of objects
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
