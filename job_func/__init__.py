# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:09:11 2019

@author: JMN
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from job_func.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from job_func.routes import get_jobs

    return app
