# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:0000/digital_waste_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_super_secret_key'
