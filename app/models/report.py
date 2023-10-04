from sqlalchemy import Column, String, Integer, Float,orm,ForeignKey,Date
from app.models.base import Base
from sqlalchemy.orm import relationship

class Report(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    year =Column(Integer,nullable=False)
    totaloffers = Column(Integer)

    def __init__(self,year,totaloffers):
        self.year = year
        self.totaloffers = totaloffers
    # def jsonstr(self):

    #     jsondata = {
    #         'name':self.name,
    #         'age': self.age,
    #         'college': self.college,
    #         'email': self.email,
    #         'GPA': self.GPA

    #     }

    #     return jsondata
