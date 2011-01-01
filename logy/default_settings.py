# is the debug mode on
DEBUG = True

# !!!WARNING!!! MODIFY THIS IN PRODUCTION
SECRET_KEY = 'LOGY_?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'

# interface to bind
SERVER_HOSTNAME = '127.0.0.1'

# port to bind
SERVER_PORT = 5000

# should we use reloader to run the server
SERVER_USE_RELOADER = False 

# should we use debugger to run the server
SERVER_USE_DEBUGGER = True

# URI of database
DATABASE_URI = 'sqlite:///test.db'

# API keys for logging handlers to write record
API_KEYS = [
    'TEST'
]

# logging format to display
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# user need be authenticated to view page
NEED_AUTH = False

USERS = {
    'logy': 'logypass'
}