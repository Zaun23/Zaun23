from curses.ascii import NUL
from tkinter import font
from flask import render_template, url_for, redirect, Blueprint, flash
from flask_mail import Message
from flask_office import mail, db
from flask_office.emails.forms import EmailFormSimple
from flask_office.models import LetterInfo

email = Blueprint('email', __name__)


# ROUTE FOR GETTING A PACKAGE
@email.route('/mail/packet', methods=['GET', 'POST'])
def notify_package():
    form = EmailFormSimple()
    
    if form.validate_on_submit():
        mail_info = LetterInfo(recipent=form.recipent.data, sender_1=form.sender_1.data, sender_2=form.sender_2.data)
        
        msg = Message('Post für dich im COCOQUADRAT', sender = 'zaun3875@gmail.com', recipients = [form.recipent.data])
        
        if form.sender_2.data == "": 
            msg.body = """Hallo,
            
heute kam ein Paket für dich im Coco Quadrat an!
Beim Absender handelt es sich um:
- {sender}
            
Das Paket liegt nun in deinem Fach und wartet auf dich.
Du kannst es gerne jederzeit während unseren Öffnungszeiten abholen.
            
Liebe Grüße
Dein CocoQuadrat Team""".format(sender = form.sender_1.data)
        else:
            msg.body = """Hallo,
            
heute kam ein Paket für dich im Coco Quadrat an!
Beim Absender handelt es sich um:
- {sender1}
- {sender2}
            
Das Paket liegt nun in deinem Fach und wartet auf dich.
Du kannst es gerne jederzeit während unseren Öffnungszeiten abholen.
            
Liebe Grüße
Dein CocoQuadrat Team""".format(sender1 = form.sender_1.data, sender2 = form.sender_2.data)
        
        mail.send(msg)
        db.session.add(mail_info)
        db.session.commit()
        return redirect(url_for('core.index'))
    
    return render_template('simple_mail.html', form=form)


# ROUTE FOR GETTING A LETTER
@email.route('/mail/letter', methods=['GET', 'POST'])
def notify_letter():
    form = EmailFormSimple()
    
    if form.validate_on_submit():
        mail_info = LetterInfo(recipent=form.recipent.data, sender_1=form.sender_1.data, sender_2=form.sender_2.data)
        
        msg = Message('Post für dich im COCOQUADRAT', sender = 'zaun3875@gmail.com', recipients = [form.recipent.data])
        
        if form.sender_2.data == "":
            msg.body = """Hallo,
        
heute kam Post für dich im Coco Quadrat an!
Beim Absender handelt es sich um:
  - {sender}

Die Post liegt nun in deinem Fach und wartet auf dich.
Falls wir sie scannen sollen, gib uns bitte Bescheid!

Liebe Grüße
Dein CocoQuadrat Team""".format(sender = form.sender_1.data)
        else:
            msg.body = """Hallo,
        
heute kam Post für dich im Coco Quadrat an!
Beim Absender handelt es sich um:
  - {sender_1}
  - {sender_2}

Die Post liegt nun in deinem Fach und wartet auf dich.
Falls wir sie scannen sollen, gib uns bitte Bescheid!

Liebe Grüße
Dein CocoQuadrat Team""".format(sender_1 = form.sender_1.data, sender_2 = form.sender_2.data)
            
        mail.send(msg)
        db.session.add(mail_info)
        db.session.commit()
        return redirect(url_for('core.index'))
    
    return render_template('simple_mail.html', form=form)
    
