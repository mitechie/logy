from flask import Module, request
from logy.core import app
from logy.models import database, tables

# sink for logging records
sink = Module(__name__)

@sink.route('/<api_key>/<app_name>', methods=['POST'])
def writeLog(api_key, app_name):
    # TODO: Check api_key here)
    print api_key
    record_dict = {}
    for key, value in request.form.iteritems():
        record_dict[key] = value
    
    host = tables.Host.query.get(request.remote_addr)
    if host is None:
        host = tables.Host(ip=request.remote_addr, 
                           name=record_dict.get('_ex_host'))
        database.db_session.add(host)
        app.logger.info('Create new host %s with name %s', host.ip, host.name)
    
    record_app = tables.App.query.get(app_name)
    if record_app is None:
        record_app = tables.App(app_name)
        host.apps.append(record_app)
        database.db_session.add(record_app)
        app.logger.info('Create new app %s of host %s', 
                        record_app.name, host.ip)
    
    record = tables.Record(
        name=record_dict['name'],
        msg=record_dict['msg'],
        usename=record_dict.get('_ex_username'),
    )
    record_app.records.append(record)
    
    database.db_session.add(record)
    database.db_session.commit()
    app.logger.info('Create record of app %s', record_app.name)
    return'ok'