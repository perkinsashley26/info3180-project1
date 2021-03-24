from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileField, FileRequired

class PropertyForm(FlaskForm):
    title = StringField("Property Title", validators = [DataRequired()])

    description = TextAreaField("Description", validators = [DataRequired()])
    
    num_bedrooms = StringField("No. of Bedroom", validators = [DataRequired()])
    num_bathrooms = StringField("No. of Bathrooms", validators = [DataRequired()])

    price = StringField("Price", validators = [DataRequired()])

    propertytype = SelectField("Property Type", choices = [("house", "House"), ("apartment","Apartment")])

    location = StringField("Location", validators = [DataRequired()])
    
    
    photo = FileField("Photo", validators = [FileRequired(),FileAllowed(["jpg","png","jpeg", "Images Only!"])])