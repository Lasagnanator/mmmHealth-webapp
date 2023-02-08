from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask import Flask
from config import Config
import app.utils as u
from flask_login import LoginManager, login_user 


app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

'''gestione errore mancata connessione al DB'''
try:
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
except Exception:
    print('mancata connessione al databasse')
    pass 


#BOOTSTRAPFLASK --> framework per usare bootstrap su flask
bootstrap = Bootstrap5(app)


from app import routes
from app import models as m

@login_manager.user_loader
def load_user(user_id):
    return m.Login_doctor.get(id)