=============
What is Logy?
=============

Logy is a central logging system for Python based on Flask.  It can receive 
logging records from other servers through Internet and store them in database, 
then display it as web pages.

============
Installation
============

To install Logy:

::

    pip install logy

==============
How to use it?
==============

Before you can write some records to Logy, you need to initialize the database.  
Type and run

::

    logy_initdb

By default, it creates sqlite3 database in current directory. And to run the 
server, here type

::
    
    logy_run

And you should see following line in console

::

 * Running on http://127.0.0.1:5000/

And here you can open the browser to see the index page. But there is no 
record in database by now. To write some records to the database, you need to 
install logging handler first. To install it, type 

::

    pip install ex_loghandlers

With the extended logging handler, here is a simple python module which 
writes logging records to Logy. 

::

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

And here you can open the url http://127.0.0.1:5000/ and see those logging 
records. Here is some details of the parameters for the logging server in 
the url "/sink/TEST/myapp"

 * TEST - it is the API key for logging service
 * myapp - it is what name of application you're running now

For example, you have a server which is running three different application 
proxy01, web01 and mail01, then you can write url like this:

::

  /sink/TEST/proxy01
  /sink/TEST/web01
  /sink/TEST/mail01

=============
Configuration
=============

Of course, you won't run logy directly in production environment, you need to 
write your own configuration.  You can see the default configuration in 
logy/default_settings.py, you don't have to modify the configuration file 
directly, instead, you can copy it and modify it.  

To run the server with your own configuration, you can set up an environment 
variable, for example:

::

    LOGY_SETTINGS=myconfig.py logy_run

And here you are, the server is running with your own configuration.