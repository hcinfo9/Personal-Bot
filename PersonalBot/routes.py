from flask import render_template, url_for
from PersonalBot import app

@app.route("/", methods=["GET","POST"])
def homepage():
   return render_template('index.html')


   
   