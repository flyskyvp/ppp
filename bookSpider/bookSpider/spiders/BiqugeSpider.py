# -*- coding: utf-8 -*-
import scrapy
from bookSpider.items import BookspiderItem

class BiqugeSpider(scrapy.Spider):
    name = "bookSpider"
    allowed_domains = ["biquge.la"]
    start_urls = (
        'http://www.biquge.la/book/903/',
    )
    print 'xxxxxxxxxxxxxxxxxxxxxxstart'

    def parse(self, response):
        print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxstart parse"
        lis = response.xpath('//div[@id="list"]/dl/dd[1]')
        print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxlis',lis
        for li in lis:
            print li
            url=response.urljoin(li.xpath('a/@href')[0].extract())
            print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',url
            yield scrapy.Request(url, callback=self.parse_question)

    def parse_question(self,response):
        items = BookspiderItem()
        book_name = response.xpath('//div[@class="bookname"]/h1/text()')[0].extract()
        content = response.xpath('//div[@id="content"]/text()').extract()
        for paragraph_index,paragraph_text in enumerate(content):
            # print book_name,paragraph_index,paragraph_text
            items['book_name']=book_name
            items['paragraph_index']=paragraph_index
            items['paragraph_text']=paragraph_text
            yield items