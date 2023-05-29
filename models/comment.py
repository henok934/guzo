from models.base import BaseModel, Base
from sqlalchemy import *
class Fedback(BaseModel,Base):

    __tablename__ = 'coment'
    fullname = Column(String(30),nullable=False)
    comment = Column(String(200),nullable=False)

