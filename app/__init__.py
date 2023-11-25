from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder = '../static', template_folder="../templates")

app.config.from_pyfile('../config.py')

db = SQLAlchemy(app = app)

from . import index
app.register_blueprint(index.index_bp)