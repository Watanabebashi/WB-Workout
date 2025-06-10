from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# TODO:DB設定などのコードを書く
def create_app():
    app = Flask(__name__)
    return app