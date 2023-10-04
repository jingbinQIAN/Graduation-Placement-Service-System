from sqlalchemy import Column, String, Integer, Float,orm,ForeignKey,Date
from app.models.base import Base
from sqlalchemy.orm import relationship

class Offer(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    year =Column(Integer,nullable=False)
    photocopy = Column(String(50),nullable=True)                 
    GPA = Column(Float,nullable=False)
    reality = Column(Integer,nullable=False)
    uicer_id = Column(Integer,ForeignKey('ui_cer.id',ondelete='CASCADE'))
    uicer = relationship("UICer",backref="offer")
    #report_id = Column(Integer,ForeignKey('report.id',ondelete='CASCADE'))
    #report = relationship("Report",backref="offer")
    programe = Column(String(50),nullable=False)    
    universityname = Column(String(50),nullable=False) 

    def __init__(self,year,GPA,reality,uicer_id,universityname,programe,photocopy):
        self.year = year
        self.GPA = GPA
        self.reality = reality
        self.uicer_id = uicer_id
        self.universityname = universityname
        self.programe = programe
        self.photocopy = photocopy

    # def jsonstr(self):

    #     jsondata = {
    #         'name':self.name,
    #         'age': self.age,
    #         'college': self.college,
    #         'email': self.email,
    #         'GPA': self.GPA

    #     }

    #     return jsondata
