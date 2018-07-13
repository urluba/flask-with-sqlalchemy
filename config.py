# config.py
import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    BASIC_AUTH_USERNAME = os.environ['BASIC_AUTH_USERNAME']
    BASIC_AUTH_PASSWORD = os.environ['BASIC_AUTH_PASSWORD']
    SECRET_KEY = os.environ['SECRET_KEY']
