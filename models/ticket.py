from sqlalchemy import *
from sqlalchemy.orm import *
from models.base import Base, BaseModel

class Ticket(BaseModel,Base):
    __tablename__ = 'tickets'
    fname = Column(String(30),nullable=False)
    lname = Column(String(30),nullable=False)
    phone = Column(Integer,nullable = False,unique=True)
    gender = Column(String(4),nullable=False)
    depcity = Column(String(20),nullable=False)
    descity = Column(String(20),nullable=False)
    no_seat = Column(Integer, nullable = False, unique=True)
    price = Column(String(6),nullable=False)
    plate_no = Column(Integer, nullable=False, unique=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    def __init__(self, *args, **kwargs):
        """Initializes Order object with super class constructor"""
        super().__init__(*args, **kwargs)
