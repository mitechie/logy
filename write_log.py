import logging

import ex_loghandlers

rootLogger = logging.getLogger('')
rootLogger.setLevel(logging.DEBUG)

sream_handler = logging.StreamHandler()
# set up the http handler which writes records to Logy server
http_handler = ex_loghandlers.ExHTTPHandler(host='localhost:5000', 
                                            url='/sink/TEST/myapp', 
                                            method='POST')
rootLogger.addHandler(sream_handler)
rootLogger.addHandler(http_handler)

logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')

try:
    raise Exception("Boom")
except:
    logger1.fatal("Huston, we've got a problem", exc_info=True) 
    
logger1.info('Everything goes fine, now.')