from flask import render_template, url_for, redirect, Blueprint, flash
from flask_mail import Message
from flask_office import mail

email = Blueprint('email', __name__)


# ROUTE FOR GETTING A PACKAGE
@email.route('/mail/packet')
def notify_package():
    msg = Message('Post für dich im COCOQUADRAT', sender = 'yourId@gmail.com', recipients = ['123zaeune@gmail.com'])
    msg.body = """Hallo,
heute kam ein Paket für dich im Coco Quadrat an!
Beim Absender handelt es sich um:
  - insert Absender 1 
  - insert Absender 2
    
Das Paket liegt nun in deinem Fach und wartet auf dich.
Du kannst es gerne jederzeit während unseren Öffnungszeiten abholen.

Liebe Grüße
Dein CocoQuadrat Team"""
    mail.send(msg)
    return "Sent" 


# ROUTE FOR GETTING A LETTER
@email.route('/mail/letter')
def notify_letter():
    msg = Message('Post für dich im COCOQUADRAT', sender = 'yourId@gmail.com', recipients = ['123zaeune@gmail.com'])
    msg.body = """Hallo,
heute kam Post für dich im Coco Quadrat an!
Beim Absender handelt es sich um:
  - insert Absender 1 
  - insert Absender 2
    
Die Post liegt nun in deinem Fach und wartet auf dich.
Falls wir sie scannen sollen, gib uns bitte Bescheid!

Liebe Grüße
Dein CocoQuadrat Team"""
    mail.send(msg)
    return "Sent" 