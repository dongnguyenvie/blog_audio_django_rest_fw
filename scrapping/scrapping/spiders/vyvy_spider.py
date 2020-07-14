# https://dongnguyenvie.github.io/audiovyvy
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

class VyvySpider(Spider):
    name = "vyvy"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "https://dongnguyenvie.github.io/audiovyvy",
    ]

    def start_requests(self):
        print("start_requests")
        for url in self.start_urls:
            # yield SplashRequest(url, self.parse, endpoint='execute',
            #                     args={'lua_source': script})
            yield SplashRequest(url, self.parse, args={'wait': 5})

    def parse(self, response):
        titles = Selector(response).css('div.v-card__actions')
        print(titles)
        pages = {}
        for index, title in enumerate(titles):
            item = {}
            item['title'] = title.css(
                '::text').extract()[0]
            # item['url'] = question.xpath(
            #     'a[@class="question-hyperlink"]/@href').extract()[0]
            pages[index] = item
        print(pages)
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