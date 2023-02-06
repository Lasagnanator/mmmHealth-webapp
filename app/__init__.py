from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask import Flask
from config import Config
import app.utils as u

app = Flask(__name__)
app.config.from_object(Config)


'''gestione errore mancata connessione al DB'''
try:
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
except:
    db = 'bad request!', 400


#BOOTSTRAPFLASK --> framework per usare bootstrap su flask
bootstrap = Bootstrap5(app)


from app import routes, models

