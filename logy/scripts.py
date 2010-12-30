from distutils.core import Command

class InitdbCommand(Command):
    description = "initialize database"
    user_options = []
    
    def initialize_options(self):
        pass
    
    def finalize_options(self):
        pass
    
    def run(self):
        import logy.core
        from logy.models import database
        database.init_db()
        print 'Done.'
        
class ServeCommand(Command):
    description = "run server"
    user_options = []
    
    def initialize_options(self):
        pass
    
    def finalize_options(self):
        pass
    
    def run(self):
        from logy.core import app
        app.run(debug=True, use_reloader=False)