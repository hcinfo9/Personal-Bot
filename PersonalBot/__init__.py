from flask import Flask

app = Flask(__name__)

from PersonalBot import routes

from PersonalBot import chatbot