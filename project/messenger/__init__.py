from flask import Flask
from flask_login import LoginManager
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_pyfile("config.py")
mongo = MongoClient()
testdb = mongo['test']
lm = LoginManager()
lm.init_app(app)
from messenger import views
