import logging
import logging.config

import ex_loghandlers

rootLogger = logging.getLogger('')
rootLogger.setLevel(logging.DEBUG)

sream_handler = logging.StreamHandler()
http_handler = ex_loghandlers.ExHTTPHandler('localhost:5000', '/sink/TEST/myapp', 'POST')
rootLogger.addHandler(sream_handler)
rootLogger.addHandler(http_handler)

# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Jackdaws love my big sphinx of quartz.')

# Now, define a couple of other loggers which might represent areas in your
# application:

logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')


logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')

try:
    raise Exception("Boom")
except:
    logger1.error("Huston, we've got a problem", exc_info=True) 