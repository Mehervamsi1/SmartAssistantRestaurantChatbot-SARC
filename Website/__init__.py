from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager
from os import path

'''db = SQLAlchemy()
DB_NAME = (
        'mssql+pyodbc://smartassistantrestaurantchatbot-sarc-admin:Sar@1234@smartassistantrestaurantchatbot-sarc-server.database.windows.net:1433/sarcdb-main?'
        'driver=ODBC+Driver+18+for+SQL+Server'
    )'''
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'mssql+pyodbc://smartassistantrestaurantchatbot-sarc-admin:Sar@1234@smartassistantrestaurantchatbot-sarc-server.database.windows.net:1433/sarcdb-main?'
        'driver=ODBC+Driver+18+for+SQL+Server'
    )
    
    #db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #from .models import User, Reservation
    


    #create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

