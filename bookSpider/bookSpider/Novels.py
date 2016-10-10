from sqlalchemy import Column, String, ForeignKey, create_engine,or_,and_,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Novels(Base):
    __tablename__ = 'Novels'

    id = Column(Integer, primary_key=True)

    book_name = Column(String)
    paragraph_index = Column(Integer)
    paragraph_text = Column(String)