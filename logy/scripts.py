from distutils.core import Command

class InitdbCommand(Command):
    description = "initialize database"
    user_options = []
    
    def initialize_options(self):
        pass
    
    def finalize_options(self):
        pass
    
    def run(self):
        initdb()
        
class ServeCommand(Command):
    description = "run server"
    user_options = []
    
    def initialize_options(self):
        pass
    
    def finalize_options(self):
        pass
    
    def run(self):
        run_logy()
        
def initdb():
    import logy.core
    from logy.models import database
    database.init_db()
    print 'Done.'
        
def run_logy():
    from logy.core import app
    app.run(debug=app.config['DEBUG'], 
            host=app.config['SERVER_HOSTNAME'],
            port=app.config['SERVER_PORT'],
            use_reloader=app.config['SERVER_USE_RELOADER'],
            use_debugger=app.config['SERVER_USE_DEBUGGER'])