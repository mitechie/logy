from flask import Module, flash
from flaskext.genshi import render_response

from logy.core import app
from logy.models import tables

frontend = Module(__name__)

@frontend.route('/')
def index():
    hosts = tables.Host.query
    return render_response('index.html', dict(hosts=hosts))