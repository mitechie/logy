from sqlalchemy import Column, ForeignKey, Integer, Unicode, String
from sqlalchemy.orm import relationship

from logy.models import database

class Record(database.Base):
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    app_name = Column(Unicode(32), 
        ForeignKey('app.name', onupdate='CASCADE', ondelete='CASCADE'), 
        nullable=False)

    name = Column(Unicode())
    msg = Column(Unicode())
    username = Column(Unicode())

    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)
            
class App(database.Base):
    __tablename__ = 'app'
    
    name = Column(Unicode(32), primary_key=True)
    host_ip = Column(Unicode(32), 
        ForeignKey('host.ip', onupdate='CASCADE', ondelete='CASCADE'), 
        nullable=False)
    
    records = relationship("Record", backref="app")

    def __init__(self, name):
        self.name = name

class Host(database.Base):
    __tablename__ = 'host'
    
    ip = Column(String(32), primary_key=True)
    name = Column(Unicode())
    
    apps = relationship("App", backref="host")

    def __init__(self, ip, name):
        self.ip = ip
        self.name = name