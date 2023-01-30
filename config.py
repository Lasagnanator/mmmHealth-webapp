import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql+psycopg2://mhealth:BIGsmeni42@spectralkraken.tk:5432/mhealth'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
