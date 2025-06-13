from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# db = SQLAlchemy()
login_manager = LoginManager()
#login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'

# TODO:DB設定などのコードを書く
def create_app():
    app = Flask(__name__)
    # TODO:シークレットキーは設定ファイルで管理
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/workout'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #db.init_app(app)
    #login_manager.init_app(app)

    #with app.app_context():
        #db.create_all()
    
    return app