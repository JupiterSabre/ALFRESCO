from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_mail import Mail, Message


# YOU LEFT OFF HERE FOR THURSDAY SOMETHING WITH THE MAIL VARIABLE, FIX THE PASSWORD RESET PLEASE.
# create database
db = SQLAlchemy()
ALFREDO_USER_DB = "database.db"
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "catdogcatdog"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{ALFREDO_USER_DB}"


    # config flask_mail for password reset
    app.config['MAIL_SERVER'] = 'smtp.yourmailserver.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'your@email'
    app.config['MAIL_PASSWORD'] = 'yourpassword'
    app.config['MAIL_USE_TS'] = False
    app.config['MAIL_USE_SSL'] = True

    db.init_app(app)
    mail.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Route_Instance

    with app.app_context():
        db.create_all()

    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_member(id):
        return User.query.get(int(id))
    

    return app

def create_database(app):
    if not path.exists("Website/" + ALFREDO_USER_DB):
        db.create_all(app=app)
        print("Database created")

    
    