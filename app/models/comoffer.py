from sqlalchemy import Column, String, Integer, Float,orm,ForeignKey,Date
from app.models.base import Base
from app.models.offer import Offer
from sqlalchemy.orm import relationship

class ComOffer(Offer):

    title = Column(String(50))                 
    companyname = Column(String(50))    
    country = Column(String(50)) 
    qualification = Column(String(50)) 

    def __init__(self,year,GPA,reality,uicer_id,universityname,programe,photocopy,title, companyname,country,qualification):
        super(ComOffer,self).__init__(year,GPA,reality,uicer_id,universityname,programe,photocopy)
        self.title = title
        self.companyname = companyname
        self.country = country
        self.qualification = qualification

    # def jsonstr(self):

    #     jsondata = {
    #         'name':self.name,
    #         'age': self.age,
    #         'college': self.college,
    #         'email': self.email,
    #         'GPA': self.GPA

    #     }

    #     return jsondata
