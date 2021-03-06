from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('getmona.config')
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)

import getmona.views
