from flask import Flask
from pypyodbc as odbc
import pandas as pd
from credential import username,password

#Azure requirements
import os
import pyodbc, struct
from azure import identity

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TheContinentalGrand'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app

