import imp
from sqlite3 import DataError
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

# Form takes information about letters or packets form costumers
class EmailFormSimple(FlaskForm):
    
    recipent = EmailField("Empfänger Mail Adresse", validators=[DataRequired(), Email()])
    sender_1 = TextField("Absender", validators=[DataRequired()])
    sender_2 = TextField("Absender")
    submit = SubmitField("Submit")
    