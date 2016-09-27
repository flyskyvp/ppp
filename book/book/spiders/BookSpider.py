from scrapy.spider import Spider
from scrapy.selector import Selector
from book.items import BookContextsItem 
from scrapy.http import Request


class BookSpider(Spider):
 

    download_delay = 1
    name = "book"
    allowed_domains = ["biquge.la"]
    start_urls = [
        "http://www.biquge.la/book/903/8206117.html"
    ]


    def parse(self, response):
        item = BookContextsItem()
        sel = Selector(response)
        bookName=sel.xpath('//div[@class="con_top"]/a[@href="/book/903/"]/text()').extract()[0]
        # chapterUrl=sel.xpath('//div[@id="info"]/p/a[contains(@href,"html")]/@href').extract()[0]
        chapterName=sel.xpath('//div[@class="bookname"]/h1/text()').extract()[0]
        chapterContext=sel.xpath('//div[@id="content"]/text()').extract()[0]
        print '----------xxxxxx-------',bookName,chapterName
        print '-------==============================',chapterContext
        item['bookName']=bookName
        item['chapterName']=chapterName
        item['chapterContext']=chapterContext
        yield item

        url='http://www.biquge.la/book/903/' + sel.xpath('//div[@class="bottem2"]/a[2]/@href').extract()[0]
        print 'xxxxxxxxxxxxxxxxxxxxxxxxxx',url
        yield Request(url, callback=self.parse)

