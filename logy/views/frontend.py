from flask import Module, flash, abort
from flaskext.genshi import render_response

from logy.core import app
from logy.auth import requires_auth
from logy.models import tables

frontend = Module(__name__)

@frontend.route('/')
@requires_auth
def index():
    hosts = tables.Host.query
    return render_response('index.html', dict(hosts=hosts))

@frontend.route('/view_record/<host_ip>/<app_name>')
@requires_auth
def view_record(host_ip, app_name):
    log_app = tables.App.query.filter_by(host_ip=host_ip, name=app_name).first()
    if log_app is None:
        abort(404)
    hosts = tables.Host.query
    records = log_app.records
    log_format = app.config['LOG_FORMAT']
    return render_response('view_record.html', 
                           dict(app=log_app, 
                                records=records, 
                                hosts=hosts, 
                                log_format=log_format))