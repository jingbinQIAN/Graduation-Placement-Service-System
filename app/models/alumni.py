from sqlalchemy import Column, String, Integer, Float,orm,ForeignKey
from app.models.uicer import UICer
from sqlalchemy.orm import relationship

class Alumni(UICer):

    

    def __init__(self, name, age, college, email, password, GPA,status,gender):
        super(Alumni,self).__init__(name, age, college, email, password, GPA, status,gender)

    def jsonstr(self):

        jsondata = {
            'name':self.name,
            'age': self.age,
            'college': self.college,
            'email': self.email,
            'GPA': self.GPA

        }

        return jsondata
