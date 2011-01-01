from flask import Module, flash, abort
from flaskext.genshi import render_response

from logy.core import app
from logy.models import tables

frontend = Module(__name__)

@frontend.route('/')
def index():
    hosts = tables.Host.query
    return render_response('index.html', dict(hosts=hosts))

@frontend.route('/view_record/<host_ip>/<app_name>')
def view_record(host_ip, app_name):
    app = tables.App.query.filter_by(host_ip=host_ip, name=app_name).first()
    if app is None:
        abort(404)
    hosts = tables.Host.query
    records = app.records
    return render_response('view_record.html', 
                           dict(app=app, records=records, hosts=hosts))