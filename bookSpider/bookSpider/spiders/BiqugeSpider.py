# -*- coding: utf-8 -*-
import scrapy
from bookSpider.items import BookspiderItem

class BiqugeSpider(scrapy.Spider):
    name = "biquge"
    allowed_domains = ["biquge.la"]
    start_urls = (
        'http://www.biquge.la/book/903/',
    )

    def parse(self, response):
        lis = response.xpath('//div[@id="list"]/dl/dd')
        for li in lis:
            url=response.urljoin(li.xpath('a/@href')[0].extract())
            yield scrapy.Request(url, callback=self.parse_question)


    def parse_question(self,response):
    	items = BookspiderItem()
    	book_name = response.xpath('//div[@class="bookname"]/h1/text()')[0].extract()
    	content = response.xpath('//div[@id="content"]/text()').extract()
    	for paragraph_index,paragraph_text in enumerate(content):
    		print book_name,paragraph_index,paragraph_text
    		items['book_name']=book_name
    		items['paragraph_index']=paragraph_index
    		items['paragraph_text']=paragraph_text
    		yield items