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
        # print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxstart parse"
        self.book_name = response.xpath('//div[@id="info"]/h1/text()')[0].extract()
        lis = response.xpath('//div[@id="list"]/dl/dd')
        # print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxlis',lis
        for li in lis:
            # print li
            url=response.urljoin(li.xpath('a/@href')[0].extract())
            # print 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',url
            yield scrapy.Request(url, callback=self.parse_question)

        #test
        # url=response.xpath('//div[@id="list"]/dl/dd')[0].xpath('a/@href')[0].extract()
        # print response.urljoin(url)
        # yield scrapy.Request(response.urljoin(url), callback=self.parse_question)

    def parse_question(self,response):
        items = BookspiderItem()
        chapter_name = response.xpath('//div[@class="bookname"]/h1/text()')[0].extract()
        content = response.xpath('//div[@id="content"]/text()').extract()
        for paragraph_index,paragraph_text in enumerate(content):
            # print book_name,paragraph_index,paragraph_text
            items['book_name']=self.book_name
            items['chapter_name']=chapter_name
            items['paragraph_index']=paragraph_index
            items['paragraph_text']=paragraph_text
            yield items
            # print 'lalllalalalalalallalala',self.book_name,chapter_name,paragraph_index,paragraph_text
