from sqlalchemy import Column, String, Integer, Float,orm,ForeignKey,Date
from app.models.base import Base
from app.models.offer import Offer
from sqlalchemy.orm import relationship

class TaughtOffer(Offer):

    #role = Column(String(50))#TA or Teacher

    def __init__(self,year,GPA,reality,uicer_id,universityname,programe,photocopy):
        super(TaughtOffer,self).__init__(year,GPA,reality,uicer_id,universityname,programe,photocopy)
        #self.role = role

    # def jsonstr(self):

    #     jsondata = {
    #         'name':self.name,
    #         'age': self.age,
    #         'college': self.college,
    #         'email': self.email,
    #         'GPA': self.GPA

    #     }

    #     return jsondata
