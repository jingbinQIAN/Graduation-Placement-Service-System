from sqlalchemy import Column, String, Integer, Float,ForeignKey
from app.models.base import Base
from sqlalchemy.orm import relationship

class Program(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    universityname = Column(String(50), unique=True, nullable=False)
    GPAlow = Column(Float,nullable=False)
    GPAupper = Column(Float,nullable=False)
    university_id=Column(Integer,ForeignKey('university.id',ondelete='CASCADE'))
    university = relationship("University",backref="program")

    def __init__(self, name, universityname,GPAlow,GPAupper,university_id):
        self.name = name
        self.universityname = universityname
        self.GPAlow = GPAlow
        self.GPAupper = GPAupper
        self.university_id = university_id

