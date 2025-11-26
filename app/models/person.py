from sqlalchemy import Column,Integer,String
from app.db.session import Base

class Person(Base):
    __tablename__ = "persons"
    
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(50),nullable=False)
    email = Column(String(100),nullable=False)