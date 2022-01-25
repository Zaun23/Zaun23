from re import T
from sqlalchemy import null, true
from sqlalchemy.orm import backref
from flask_office import db
from flask_admin.contrib.sqla.view import ModelView

class LetterInfo(db.Model):
    __tablename__ = 'mail'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # information about letter / packet for costumer
    recipent = db.Column(db.String(256), nullable=False)
    sender_1 = db.Column(db.String(256), nullable=False)
    sender_2 = db.Column(db.String(256), nullable=True)
    
    # TODO add potential relation to account of user -> account for every work-adress?
    


# data class for storing room bookings
class RoomBooking(db.Model):
    __tablename__ = 'bookings'

    # costumer = db.relationship(Costumer)

    id = db.Column(db.Integer, primary_key=True)
    
    # Information about the room
    room = db.Column(db.String(256), nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_at = db.Column(db.Time())
    end_at = db.Column(db.Time())
    price = db.Column(db.Float())
    
    # Inforamtion about costumer
    company = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    adress = db.Column(db.String(128), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(64), nullable=False)
    land = db.Column(db.String(64), nullable=False)

    # TODO add potential relationship to booked catering for given meeting

