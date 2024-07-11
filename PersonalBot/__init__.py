from flask import Flask # type: ignore

app = Flask(__name__)

from PersonalBot import routes

from PersonalBot import chatbot