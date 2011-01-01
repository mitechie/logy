import datetimefrom flask import Module, request, abort
from logy.core import app
from logy.models import database, tables

# sink for logging records
sink = Module(__name__)

@sink.route('/<api_key>/<app_name>', methods=['POST'])
def writeLog(api_key, app_name):    if api_key not in app.config['API_KEYS']:
        abort(403)
    record_dict = {}
    for key, value in request.form.iteritems():
        record_dict[key] = value
        host_ip = request.remote_addr
    host = tables.Host.query.get(host_ip)
    if host is None:
        host = tables.Host(ip=host_ip, 
                           name=record_dict.get('_ex_hostname'))
        database.db_session.add(host)
        app.logger.info('Create new host %s with name %s', host.ip, host.name)
    
    record_app = tables.App.query. \        filter_by(host_ip=host_ip, name=app_name).first()
    if record_app is None:
        record_app = tables.App(app_name)
        host.apps.append(record_app)
        database.db_session.add(record_app)
        app.logger.info('Create new app %s of host %s', 
                        record_app.name, host.ip)            created = None    if record_dict.get('created') is not None:        created = datetime.datetime.fromtimestamp(float(record_dict['created']))            msecs = None    if record_dict.get('msecs') is not None:        msecs = float(record_dict['msecs'])
    record = tables.Record(
        name=record_dict.get('name'),
        levelno=record_dict.get('levelno'),        levelname=record_dict.get('levelname'),        pathname=record_dict.get('pathname'),        filename=record_dict.get('filename'),        module=record_dict.get('module'),        funcName=record_dict.get('funcName'),        lineno=record_dict.get('lineno'),        created=created,        msecs=msecs,        thread=record_dict.get('thread'),        threadName=record_dict.get('threadName'),        process=record_dict.get('process'),        processName=record_dict.get('processName'),        message=record_dict.get('message'),
        username=record_dict.get('_ex_username'),        traceback=record_dict.get('_ex_traceback')
    )
    record_app.records.append(record)
    
    database.db_session.add(record)
    database.db_session.commit()
    app.logger.info('Create record of app %s', record_app.name)
    return 'ok'