# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import Column, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
from bookSpider.items import BookspiderItem
from bookSpider.Novels import Novels



class BookspiderPipeline(object):


    def open_spider(self, spider):
    	# 创建对象的基类:
        self.Base = declarative_base()
        self.engine = create_engine('mysql+pymysql://root:x@localhost/test?charset=utf8',echo=True)
        self.DBSession = sessionmaker(bind=self.engine)
        
        self.session = self.DBSession()


    def process_item(self, item, spider):
        a = Novels(
                    book_name=item["book_name"].encode("utf-8"),
                    paragraph_index=item["paragraph_index"],
                    paragraph_text=item["paragraph_text"].encode("utf-8")
                   )
        self.Base.metadata.create_all(self.engine)
  
        self.session.add(a)
        self.session.commit()

    def close_spider(self,spider):
        self.session.commit()
        self.session.close()