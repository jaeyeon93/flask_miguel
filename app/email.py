# -*- coding:utf-8 -*-

from flask_mail import Mail, Message
from flask import render_template, app
from threading import Thread

# email
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template+'.txt',**kwargs)
    msg.html = render_template(template+'.html',**kwargs)
    mail.send(msg)

def send_async_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX']+subject, sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body = render_template(template,'.txt',**kwargs)
    msg.html = render_template(template,'.html',**kwargs)
    thr = Thread(target=send_async_email, args=[app,msg])
    thr.start()
    return thr