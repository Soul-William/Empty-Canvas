from web import app
from flask import render_template

@app.route('/')
def landingpage():
    return render_template('landingPage.html')
