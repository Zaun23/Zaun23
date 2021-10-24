from flask import render_template, url_for, redirect, Blueprint, flash
from flask_office import db
from flask_office.models import RoomBooking
from flask_office.bookings.forms import BookingFormSimple

# TODO add views for the questionaire that then creates the proposal
bookings = Blueprint('bookings', __name__)


# SIMPLE BOOKING WITHOUT CATERING
@bookings.route('/bookings/simple', methods=['GET', 'POST'])
def simple_booking():
    form = BookingFormSimple()

    if form.validate_on_submit():
        booking = RoomBooking(room=form.room.data, date=form.date.data, start_at=form.start_at.data, end_at=form.end_at.data,
                              company=form.company.data, name=form.name.data, adress=form.adress.data,
                              zip_code=form.zip_code.data, city=form.city.data, land=form.land.data)
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('core.index'))

    return render_template('simple_booking.html', form=form)
