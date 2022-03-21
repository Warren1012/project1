from flask_wtf import FlaskForm
from wtforms import StringField,FileField,DecimalField,IntegerField,SelectField,TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class Propertyform(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    rooms = IntegerField('rooms', validators=[DataRequired()])
    bathroom = IntegerField('bathroom', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    price = DecimalField('price', validators=[DataRequired()])
    type=SelectField('Type',choices=[('House','House'),('Apartment','Apartment')],validators=[DataRequired()])
    description=TextAreaField('description',validators=[DataRequired()])
    image = FileField('image', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
    