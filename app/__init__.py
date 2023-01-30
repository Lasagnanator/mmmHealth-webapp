from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#BOOTSTRAPFLASK --> framework per usare bootstrap su flask
# richiede installazione di un pacchetto 
bootstrap = Bootstrap5(app)


from app import routes, models
