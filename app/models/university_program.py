from sqlalchemy import Column, String, Integer, Float,ForeignKey
from app.models.base import Base


class Programlist(Base):
    university_id=Column(Integer,ForeignKey('university.id',ondelete='CASCADE'))
    program_id = Column(Integer,ForeignKey('program.id',ondelete='CASCADE'))
    id = Column(Integer, primary_key=True, autoincrement=True)


    def __init__(self, university_id, program_id):
        self.university_id = university_id
        self.program_id = program_id

