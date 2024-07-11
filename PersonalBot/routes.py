from flask import render_template # type: ignore
from PersonalBot import app

@app.route("/", methods=["GET","POST"])
def homepage():
   return render_template('index.html')


   
   