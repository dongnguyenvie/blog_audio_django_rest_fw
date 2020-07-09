from scrapy import Spider
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess
# from test_crawl.items import TestCrawlItem
from scrapy_splash import SplashRequest

script = """
function main(splash)
    splash:init_cookies(splash.args.cookies)
    local url = splash.args.url
    assert(splash:go(url))
    assert(splash:wait(5))
    return {
        cookies = splash:get_cookies(),
        html = splash:html()
    }
end
"""

script2 = """
function main(splash)
    splash:init_cookies(splash.args.cookies)
    local url = splash.args.url
    assert(splash:go(url))
    assert(splash:wait(0.5))
    return {
        cookies = splash:get_cookies(),
        html = splash:html()
    }
end
"""

class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='execute',
                                args={'lua_source': script})

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        pages = {}

        for index, question in enumerate(questions):
            item = {}
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            pages[index] = item
        yield pages
        
# process = CrawlerProcess(settings={
#     'LOG_LEVEL': 'ERROR',
#     'ITEM_PIPELINES': {
#         'process_item': 300,
#     }
# })
# process.crawl(StackSpider)
# process.start()

# def process_item(self, item, spider):
#     print(">>>>>>>================")
#     print(item)
#     print("====================<<<<<<<<<<<")
#     return item