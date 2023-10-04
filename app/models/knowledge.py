from sqlalchemy import Column, String, Integer, Float,orm,ForeignKey
from app.models.base import Base
from sqlalchemy.orm import relationship

class Knowledge(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    alu_id=Column(Integer,ForeignKey('ui_cer.id',ondelete='CASCADE'))
    program_id = Column(Integer,ForeignKey('program.id',ondelete='CASCADE'))
    alumniname = Column(String(50), nullable=False)
    coursename = Column(String(50), nullable=False)
    universityname = Column(String(50), nullable=False)
    programname = Column(String(50), nullable=False)
    alumni = relationship("Alumni",backref="knowledge")
    program = relationship("Program",backref="knowledge")
    comment = Column(String(200), nullable=False)
    year_visible = Column(Integer)
    gender_visible = Column(Integer)
    name_visible = Column(Integer)
    
    def __init__(self,alumniname,coursename,universityname, programname,alu_id,program_id,comment, year_visible, gender_visible, name_visible):
        self.alumniname = alumniname
        self.coursename = coursename
        self.universityname = universityname
        self.programname = programname
        self.alu_id = alu_id
        self.program_id = program_id
        self.comment = comment
        self.year_visible = year_visible
        self.gender_visible = gender_visible
        self.name_visible = name_visible
    # def jsonstr(self):

    #     jsondata = {
    #         'name':self.name,
    #         'age': self.age,
    #         'college': self.college,
    #         'email': self.email,
    #         'GPA': self.GPA

    #     }

    #     return jsondata
