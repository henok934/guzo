from models.base import Base
from models.base import BaseModel
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import ForeignKey
class Route(Base,BaseModel):
    __tablename__ = "routes"
    depcity = Column(String(20), nullable = False)
    decity = Column(String(20), nullable = False)
    kilometer = Column(Float(4),nullable = False)
    price = Column(Float(6), nullable = False)
    plate_no = Column(Integer, nullable = False, unique = True)
    bus_id = Column(String(60), ForeignKey('buses.id'),nullable = False)
    def __init__(self, *args, **kwargs):
        """Initializes City object with super class constructor"""
        super().__init__(*args, **kwargs)
