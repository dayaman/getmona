from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('getmona.config')
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)

import getmona.views
