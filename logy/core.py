from flask import Flask

app = Flask(__name__)

# create url mapping
from logy.views.sink import sink
app.register_module(sink, url_prefix='/sink')

# init database
from logy.models import database, tables

# clean database after request
@app.after_request
def shutdown_session(response):
    database.db_session.remove()
    return response