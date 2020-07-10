# https://dongnguyenvie.github.io/audiovyvy
from scrapy import Spider, Request
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

class TruyenaudioSpider(Spider):
    name = "TruyenaudioSpider"
    allowed_domains = ["truyenaudio.org"]
    start_urls = [
        "https://truyenaudio.org/kiem-hiep/",
        # "https://truyenaudio.org/kiem-hiep/?page=3"
    ]

    def start_requests(self):
        print("start_requests")
        for url in self.start_urls:
            # yield SplashRequest(url, self.parse, endpoint='execute',
            #                     args={'lua_source': script})
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        print("def parse")
        products = Selector(response).css('.v-blog-wrap .v-blog-items-wrap .category-product .category-product-item')
        pages = {}
        for index, product in enumerate(products):
            item = {}
            urlProduct = product.css('a.product-image::attr(href)').get()
            item['title'] = product.css('div.p-name h4 a::text').get().strip()
            item['img'] = product.css('a.product-image img::attr(src)').get()
            item['href'] = urlProduct
            rs = yield SplashRequest(urlProduct, self.parse_detail, args={'wait': 0.5})
            print(rs)
            print("aaaaaaaaaaaaaaaaaaaaaaa")
            # pages[index] = item
            yield item
        # yield pages
        # next_page = response.css('.dataTables_paginate ul.pagination li:nth-child(6) a::attr(href)').get()
        # if next_page is not None and next_page != 'javascript:void(0)':
        #     next_page = response.urljoin(next_page)
        #     print(next_page)
        #     yield Request(next_page, callback=self.parse)
    def parse_detail(self, response):
        print(112222)
        return "response"
        
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