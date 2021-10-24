from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, SelectField, RadioField, IntegerField, StringField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired


# Form to take information form simple bookings without catering
class BookingFormSimple(FlaskForm):

    # Information about room
    room = SelectField(u'Welchen Raum möchtest du buchen?', choices=[
      ('Ristretto', 'Meetingraum Ristretto'), ('Espresso', 'Meetingraum Espresso'),
      ('Macchiato', 'Meetingraum Macchiato'), ('Cappuccino', 'Meetingraum Cappuccino'),
      ('Lungo', 'Meetingraum Lungo'), ('Schlossbergblick', 'Meetingraum Schlossbergblick')],
      validators=[DataRequired()])
    date = DateField('Wann willst du den Raum buchen?', format='%Y-%m-%d', validators=[DataRequired()])
    start_at = TimeField('Start: ', format='%H:%M', validators=[DataRequired()])
    end_at = TimeField('Ende: ', format='%H:%M', validators=[DataRequired()])
    
    # Information about costumer
    company = StringField("Firma: ", validators=[DataRequired()])
    name = StringField("Kundenname: ", validators=[DataRequired()])
    adress = StringField("Adresse: ", validators=[DataRequired()])
    zip_code = IntegerField("Postleitzahl: ", validators=[DataRequired()])
    city = StringField("Stadt: ", validators=[DataRequired()]) 
    land = StringField("Land: ", validators=[DataRequired()])
    submit = SubmitField("Submit")