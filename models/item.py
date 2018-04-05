from db import db

# db Model indicates the class are things that are saved to and
# retrieved from the database, i.e. mapping between objects and database
class ItemModel(db.Model):
    # defining the mapped table and columnsand must be matched
    # with the object properties.
    __tablename__ = 'items'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    # because there is a store id SQL Alchemy can find the store in store table
    store = db.relationship('StoreModel')


    def __init__(self, name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    # convert item model to JSON representation
    def json(self):
        return {"name":self.name, "price": self.price}

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
