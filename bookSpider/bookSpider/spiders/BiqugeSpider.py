# -*- coding: utf-8 -*-
import scrapy
from bookSpider.items import BookspiderItem

class BiqugeSpider(scrapy.Spider):
    handle_httpstatus_list = [301]
    name = "bookSpider"
    allowed_domains = ["qu.la"]
    start_urls = (
        'http://www.qu.la/book/903/',
    )
    print 'xxxxxxxxxxxxxxxxxxxxxxstart'

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        "Host":"www.qu.la",
        "Referer": "http://www.qu.la/book/903/",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
    }

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
            print 'hhhhhhhhhhh----------------------',self.book_name,chapter_name,paragraph_index,paragraph_text
            
            yield items
            # print 'lalllalalalalalallalala',self.book_name,chapter_name,paragraph_index,paragraph_text
