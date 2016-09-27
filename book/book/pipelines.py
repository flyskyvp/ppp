# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem

import pymysql

#连接数据库
class MySQLStorePipeline(object):

    def __init__(self):
        self.conn= pymysql.connect(host='localhost', port=3306, user='root', passwd='x',charset='UTF8')
        self.cur=self.conn.cursor() #获取一个游标对象

    #pipeline默认调用
    def process_item(self, item, spider):
        self.cur.execute("CREATE DATABASE IF NOT EXISTS test DEFAULT CHARSET utf8 COLLATE utf8_general_ci;USE test;")   #创建数据库
        self.cur.execute("CREATE TABLE if not exists books (book_name VARCHAR(18),chapter_name varchar(100),chapter_context text)")#创建表
        sql="INSERT INTO books(book_name,chapter_name,chapter_context) VALUES('"+item['bookName']+"','"+item['chapterName']+"','"+item['chapterContext']+"');"
        print 'begin++++++++++++++++++++++++++++++++++++++++++++',sql,'+++++++++++++++++++++++++++++++++++++++end'
        self.cur.execute(sql)#插入数据
        self.conn.commit()
        # self.conn.close()
        # self.cur.close()
        return item