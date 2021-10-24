import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'geheim69'


#######################
### DATABASE SETUP ###
#####################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


###################
### MAIL SETUP ###
#################

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '123zaeune@gmail.com'
app.config['MAIL_PASSWORD'] = 'piraten1998'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


#############################
### IMPORTING BLUEPRINTS ###
###########################

from flask_office.core.views import core
from flask_office.bookings.views import bookings
from flask_office.admin.views import app as admin
from flask_office.emails.views import email

app.register_blueprint(core)
app.register_blueprint(bookings)
app.register_blueprint(admin)
app.register_blueprint(email)