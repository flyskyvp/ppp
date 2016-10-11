# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import Column, String, ForeignKey, create_engine,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from bookSpider.items import BookspiderItem
# from bookSpider.Novels import Novels

Base = declarative_base()

class Novels(Base):
    __tablename__ = 'Novels'

    id = Column(Integer, primary_key=True)

    book_name = Column(String(100))
    paragraph_index = Column(Integer)
    paragraph_text = Column(String(4000))

class BookspiderPipeline(object):

    def process_item(self, item, spider):
        engine = create_engine('mysql+pymysql://root:x@localhost/test?charset=utf8',echo=True)
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        a = Novels(
                    book_name=item["book_name"],
                    paragraph_index=item["paragraph_index"],
                    paragraph_text=item["paragraph_text"]
                   )
  
        Base.metadata.create_all(engine)
        session.add(a)
        session.commit()
        sesession.close()