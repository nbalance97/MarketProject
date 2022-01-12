
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Market.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# secrets.token_hex(16)
app.secret_key = '3e7e6028c343b0bc9abe4adbf2c781e0'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


