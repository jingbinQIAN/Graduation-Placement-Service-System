from sqlalchemy import Column, String, Integer, Float
from app.models.base import Base


class University(Base):
    name = Column(String(50), nullable=False)
    programlist = Column(String(50), unique=False, nullable=True)
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(50), unique=True, nullable=False)

    def __init__(self, name, programlist,city):
        self.name = name
        self.programlist = programlist
        self.city = city

