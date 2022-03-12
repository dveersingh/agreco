import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

UPLOAD_FOLDER = './static/upload'
app = Flask(__name__,static_folder='static')
app.secret_key = "36567576vhvf667rgcgccc"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ \
                os.path.join(basedir, 'mf.sqlite3')

db = SQLAlchemy(app)
ma = Marshmallow(app)

if __name__ == '__main__':
	from views import *
	app.run(debug=True)


