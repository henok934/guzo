from sqlalchemy import *
from models.base import Base,BaseModel
from sqlalchemy.orm import relationship
from hashlib import md5

class User(Base, BaseModel):
    __tablename__ = 'users'
    fname = Column(String(20),nullable = False)
    lname = Column(String(20),nullable = False)
    username = Column(String(20),nullable = False,unique = True)
    password = Column(String(10),nullable = False)
    gender = Column(String(5),nullable = False)
    phone = Column(Integer,nullable = False, unique=True)
    email = Column(String(30),nullable = False, unique = True)
    
    tickets = relationship("Ticket", backref="users")

    def __init__(self, *args, **kwargs):
        """Initializes User object with super class constructor"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
