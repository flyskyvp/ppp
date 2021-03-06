# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookspiderItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    chapter_name = scrapy.Field()
    paragraph_index = scrapy.Field()
    paragraph_text = scrapy.Field()
