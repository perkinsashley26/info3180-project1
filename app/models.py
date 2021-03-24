from . import db

class PropertyList(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    description = db.Column(db.String(255))
    num_bedrooms = db.Column(db.String(20))
    num_bathrooms = db.Column(db.String(20))
    price = db.Column(db.String(50))
    propertytype = db.Column(db.String(100))
    location = db.Column(db.String(150))
    photo = db.Column(db.String(255)) 

    def __init__(self, title, description, num_bedrooms, num_bathrooms, price, propertytype, location, photo):
        self.title = title
        self.description = description
        self.num_bedrooms=num_bedrooms
        self.num_bathrooms=num_bathrooms
        self.price = price
        self.propertytype = propertytype
        self.location = location
        self.photo=photo