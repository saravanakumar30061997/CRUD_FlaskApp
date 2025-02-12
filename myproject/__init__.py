import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Use PostgreSQL from Railway
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'database.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app,db)

from myproject.puppies.views import puppies_blueprint
from myproject.owners.views import owners_blueprints

app.register_blueprint(owners_blueprints,url_prefix='/owners')
app.register_blueprint(puppies_blueprint,url_prefix='/puppies')
