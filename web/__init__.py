from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ba7c61898fbe67c3187a7bc3'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'kwsd.webcom'
app.config['MAIL_PASSWORD'] = 'irwmckwkkfwpovbt'

mail = Mail(app)

from web import routes
