from flask import render_template
from DocumentosSite import app




@app.route ( "/" )
def home():
    return render_template('home.html')

