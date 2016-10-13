# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request, FormRequest
from zhihuSpider.items import ZhihuspiderItem

class ZhihuSpider(CrawlSpider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
        "http://www.zhihu.com"
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow = ('/question/\d+#.*?', )), callback = 'parse_page', follow = True),
        Rule(SgmlLinkExtractor(allow = ('/question/\d+', )), callback = 'parse_page', follow = True),
    )
    headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
    "Access-Control-Allow-Credentials":"true",
    "Access-Control-Allow-Origin:http":"//www.zhihu.com",
    "Cache-Control":"max-age=0, no-cache, no-store",
    "Connection":"keep-alive",
    "Content-Length":"185",
    "Content-Type":"application/json",
    "Pragma":"no-cache",
    "Server":"ZWS",
    "Vary":"Accept-Encoding",
    "X-Frame-Options":"DENY"
    }

    #重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        return [Request("http://www.zhihu.com", meta = {'cookiejar' : 1}, callback = self.post_login)]

    #FormRequeset出问题了
    def post_login(self, response):
        print 'Preparing login'
        #下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        print '-----------------------------------------------',xsrf
        #FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        #登陆成功后, 会调用after_login回调函数
        return [FormRequest.from_response(response,   #"http://www.zhihu.com/login",
                            meta = {'cookiejar' : response.meta['cookiejar']},
                            headers = self.headers,  #注意此处的headers
                            formdata = {
                            '_xsrf': xsrf,
                            'email': '1025152984@qq.com',
                            'password': 'srbrybxwcg'
                            },
                            callback = self.after_login,
                            dont_filter = True
                            )]

    def after_login(self, response) :
        for url in self.start_urls :
            yield self.make_requests_from_url(url)

    def parse_page(self, response):
        problem = Selector(response)
        item = ZhihuspiderItem()
        item['url'] = response.url
        # item['name'] = problem.xpath('//span[@class="name"]/text()').extract()
        print item['name']
        # item['title'] = problem.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        item['description'] = problem.xpath('//div[@class="zm-editable-content"]/text()').extract()
        # item['answer']= problem.xpath('//div[@class=" zm-editable-content clearfix"]/text()').extract()
        # return item

        print item['description']