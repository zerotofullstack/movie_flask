from flask import Flask

app = Flask(__name__)
app.debug = True

from app.web import web as web_blueprint
from app.admin import admin  as admin_blueprint

app.register_blueprint(web_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")