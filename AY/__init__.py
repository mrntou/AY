from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin

import json


app = Flask(__name__)
app.config.from_file('config.json',load=json.load)


db = SQLAlchemy(app)
login_manager = LoginManager(app)
admin = Admin()



# from AY import routes
from AY.routes.admin.routes import admin

app.register_blueprint(admin)



