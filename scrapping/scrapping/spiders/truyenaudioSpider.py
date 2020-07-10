# https://dongnguyenvie.github.io/audiovyvy
from scrapy import Spider, Request
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess
# from test_crawl.items import TestCrawlItem
from scrapy_splash import SplashRequest
import re
from urllib.parse import unquote

load_page_script = """
function main(splash)
    splash:init_cookies(splash.args.cookies)
    local num_scrolls = 10
    local scroll_delay = 1
    local url = splash.args.url
    local cookies = splash:get_cookies()
    local scroll_to = splash:jsfunc("window.scrollTo")
    local get_body_height = splash:jsfunc(
        "function() {return document.body.scrollHeight;}"
    )
    assert(splash:go(url))
    splash:wait(splash.args.wait)
    for _ = 1, num_scrolls do
        local height = get_body_height()
        for i = 1, 10 do
            scroll_to(0, height * i/10)
            splash:wait(scroll_delay/10)
        end
    end
    return splash:html()
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
            yield SplashRequest(url, self.parse, endpoint='execute', args={'lua_source': load_page_script, 'wait': 3})

    def parse(self, response):
        print("def parse")
        products = Selector(response).css(
            '.v-blog-wrap .v-blog-items-wrap .category-product .category-product-item')
        pages = {}
        for index, product in enumerate(products):
            item = {}
            urlProduct = product.css('a.product-image::attr(href)').get()
            arrSplitUrlProduct = urlProduct.split("/")
            arrSplitUrlProduct.insert(4, "nghe-truyen")
            urlProduct = "/".join(arrSplitUrlProduct)

            item['title'] = product.css('div.p-name h4 a::text').get().strip()
            item['img'] = product.css('a.product-image img::attr(src)').get()
            item['href'] = urlProduct
            # Crawl detail
            yield SplashRequest(urlProduct, meta={'item': item}, callback=self.parse_detail,  endpoint='execute', args={'lua_source': load_page_script, 'wait': 3})

        next_page = response.css(
            '.dataTables_paginate ul.pagination li:nth-child(6) a::attr(href)').get()
        if next_page is not None and next_page != 'javascript:void(0)':
            next_page = response.urljoin(next_page)
            print(next_page)
            yield Request(next_page, callback=self.parse)

    def parse_detail(self, response):
        item = response.request.meta['item']
        product = Selector(response).css('article.portfolio-article')
        title = product.css('h1 a::text').get()
        script = product.css(
            '#new-player > div > script:nth-child(1)::text').get()
        listUrlMp3 = [x.group() for x in re.finditer(
            r'(https?|ftp|file):\/\/(www.)?(.*?)\.(mp3)', script)]
        item["resource"] = list(map(lambda link: link, listUrlMp3))
        yield item
