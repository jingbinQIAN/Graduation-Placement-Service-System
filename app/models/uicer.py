from sqlalchemy import Column, String, Integer, Float,orm,Enum
from app.models.base import Base


class UICer(Base):
    name = Column(String(50), nullable=False)
    age = Column(Integer,nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    _password = Column('password', String(100),nullable=False)

    id = Column(Integer, primary_key=True, autoincrement=True)
    college = Column(String(50), nullable=False)
    GPA = Column(Float,nullable=False)
    status = Column(Integer,nullable=False)
    gender = Column(Enum('male','female'),nullable=False)

    def __init__(self, name, age, college, email, password, GPA, status,gender):
        self.name = name
        self.age = age
        self.email = email
        self._password = password
        self.college = college
        self.GPA = GPA
        self.status = status
        self.gender = gender

    def jsonstr(self):

        jsondata = {
            'name':self.name,
            'age': self.age,
            'college': self.college,
            'email': self.email,
            'GPA': self.GPA

        }

        return jsondata
