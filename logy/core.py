import os

from flask import Flask
from flaskext.genshi import Genshi

app = Flask(__name__, '/static')
app.config.from_object('logy.default_settings')
if 'LOGY_SETTINGS' in os.environ:
    app.config.from_envvar('LOGY_SETTINGS')
# make sure the SECRET_KEY is changed in production environment
if not app.config['DEBUG']:
    from logy import default_settings
    if app.config['SECRET_KEY'] == default_settings.SECRET_KEY:
        raise RuntimeError(
            'SECRET_KEY should be changed in production environment')
genshi = Genshi(app)

# create url mapping
from logy.views.sink import sink
from logy.views.frontend import frontend
app.register_module(sink, url_prefix='/sink')
app.register_module(frontend)

# init database
from logy.models import database, tables

# clean database after request
@app.after_request
def shutdown_session(response):
    database.db_session.remove()
    return response