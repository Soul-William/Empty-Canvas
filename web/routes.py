from web import app, mail
from flask import render_template, redirect, request, url_for, flash
from flask_mail import Message
from datetime import datetime, date
import logging, os


def send_email(subject, message):
    recipient = 'bornkenneth18@gmail.com'
    subject = subject
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
    msg.html = render_template('emailtemp.html', message=message)
    mail.send(msg)

def error_log(e):
    today = date.today()
    current_date = today.strftime("%B %d, %Y")

    now = datetime.now()
    current_time = now.strftime("%I:%M %p")

    log_date = datetime.now().strftime('%I-%M-%S %p %d-%b-%Y')
    uniq_log = os.urandom(2).hex()
    log_filename = f'error-{log_date}-{uniq_log}.text'
    error_log = f"\nTimestamp: {current_date}, {current_time} \nURL: {request.path}, \nError: {str(e)}\n------------\n\n"

    filepath = os.path.join('logs', log_filename)
    f = open(filepath, "x")
    f.write(error_log)

    subject = 'Error Log'
    message = error_log
    send_email(subject, message)

def error_log2(e):
    today = date.today()
    current_date = today.strftime("%B %d, %Y")

    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    uniq_log = os.urandom(2).hex()

    log_filename = 'error-{}-{}.log'.format(datetime.now().strftime('%I-%M-%S %p %d-%b-%Y'), uniq_log)
    log_filepath = os.path.join('logs', log_filename)
    logging.basicConfig(filename=log_filepath, level=logging.ERROR)
    logging.error(f"\n------------\nTimestamp: {current_date},{current_time} \nURL: {request.path}, \nError: {str(e)}\n------------\n\n")


# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    error_log(e)
    flash('Page not found.')
    return redirect(request.referrer or url_for('landingpage'))

@app.errorhandler(Exception)
def handle_exception(e):
    error_log(e)
    referrer = request.referrer
    flash('HTML not found.')
    return redirect(referrer or '/')


@app.route('/')
def landingpage():
    return render_template('landingPage.html')

@app.route('/try')
def trys():
    return render_template('tryPage.html')

@app.route('/send_email')
def send_email2():
    recipient = 'bornkenneth18@gmail.com'
    subject = 'Subject of the email'
    message_body = 'Body of the email'
    msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
    msg.html = render_template('emailtemp.html', message_body=message_body)
    mail.send(msg)
    return 'Email sent'


