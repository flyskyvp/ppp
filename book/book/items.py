# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BookItem(Item):
    # define the fields for your item here like:
    bookName = Field()
    chapterName = Field()
    chapterUrl = Field()

class BookContextsItem(Item):
    # define the fields for your item here like:
    bookName = Field()
    chapterName = Field()
    chapterContext = Field()