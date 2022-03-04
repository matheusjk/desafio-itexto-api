from flask import Flask, request, flash, url_for, redirect, jsonify, Response, make_response, current_app, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import datetime

db = SQLAlchemy()

def create_app():  # or def create_app(config_class=Config)

    app = Flask(__name__)

    app.config.from_object("config.DevelopmentConfig")  # or app.config.from_object(config_class)


    # db = SQLAlchemy(app)
    
    # from app.models.tables import db
    db.init_app(app)

    from app.api.routes import api


    app.register_blueprint(api)

    return app


with create_app().app_context():

    db.reflect()