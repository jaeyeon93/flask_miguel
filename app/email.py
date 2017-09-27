# -*- coding:utf-8 -*-

from flask_mail import Mail, Message
from flask import render_template, app, current_app
from threading import Thread
from . import mail # __init__
'''
# email
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
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
'''
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr