from sqlalchemy import Column, ForeignKey, Integer, Unicode, String, DateTime, \
    Float
from sqlalchemy.orm import relationship

from logy.models import database

class Record(database.Base):
    __tablename__ = 'record'
    
    id = Column(Integer, primary_key=True)
    app_name = Column(Unicode(32), 
        ForeignKey('app.name', onupdate='CASCADE', ondelete='CASCADE'), 
        nullable=False, index=True)

    # Refnerence to:
    # http://docs.python.org/library/logging.html#formatter-objects
    name = Column(Unicode(), nullable=False)
    levelno = Column(Integer(), nullable=False)
    levelname = Column(Unicode(), nullable=False)
    pathname = Column(Unicode())
    filename = Column(Unicode(), nullable=False)
    module = Column(Unicode(), nullable=False)
    funcName = Column(Unicode(), nullable=False)
    lineno = Column(Integer())
    created = Column(DateTime(), nullable=False)
    thread = Column(Integer())
    threadName = Column(Unicode())
    process = Column(Integer())
    processName = Column(Unicode())
    message = Column(Unicode(), nullable=False)
    
    username = Column(Unicode())
    traceback = Column(Unicode())

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)
            
class App(database.Base):
    __tablename__ = 'app'
    
    id = Column(Integer, primary_key=True)
    host_ip = Column(Unicode(32), 
        ForeignKey('host.ip', onupdate='CASCADE', ondelete='CASCADE'), 
        nullable=False, index=True)
    name = Column(Unicode(32), index=True)
    
    records = relationship("Record", backref="app")

    def __init__(self, name):
        self.name = name

class Host(database.Base):
    __tablename__ = 'host'
    
    ip = Column(String(32), primary_key=True)
    name = Column(Unicode(), index=True)
    
    apps = relationship("App", backref="host")

    def __init__(self, ip, name):
        self.ip = ip
        self.name = name