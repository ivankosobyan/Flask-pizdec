from sqlalchemy import Integer,String,Column,DateTime
from sqlalchemy.sql import func

from db import db

class Doctors(db.Model):
    id = Column(Integer,primary_key=True)
    name = Column(String(150))
    surname = Column(String(150))
    specialization = Column(String)
    created_at = Column(DateTime,default=func.now())
    updated_at = Column(DateTime,onupdate=func.now())

class Services(db.Model):
    id = Column(Integer,primary_key=True)
    tipe = Column(String(300))
    title = Column(String(300))
    prise = Column(Integer)
    created_at = Column(DateTime,default=func.now())
    updated_at = Column(DateTime,onupdate=func.now())