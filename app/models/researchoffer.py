from sqlalchemy import Column, String, Integer, Float,orm,ForeignKey,Date,Boolean
from app.models.base import Base
from app.models.tcoffer import TaughtOffer
from sqlalchemy.orm import relationship

class ResearchOffer(TaughtOffer):

    supervisor = Column(String(50))      
    #name = Column(String(50))
    researchtopic = Column(String(50))   
    nopapers = Column(Integer)
    noresearch = Column(Integer)


    def __init__(self,year,GPA,reality,uicer_id,universityname,programe,photocopy,supervisor,researchtopic,nopapers,noresearch):
        super(ResearchOffer,self).__init__(year,GPA,reality,uicer_id,universityname,programe,photocopy)
        self.supervisor = supervisor
        #self.name = name
        self.researchtopic = researchtopic
        self.nopapers = nopapers
        self.noresearch = noresearch

    # def jsonstr(self):

    #     jsondata = {
    #         'name':self.name,
    #         'age': self.age,
    #         'college': self.college,
    #         'email': self.email,
    #         'GPA': self.GPA

    #     }

    #     return jsondata
