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
        "https://truyenaudio.org/all/",
        # "https://truyenaudio.org/kiem-hiep/?page=3",
        # "https://truyenaudio.org/kiem-hiep/?page=1"
    ]
    dataCrawled = 0
    totalCrawled = 0

    def start_requests(self):
        print("start_requests")
        for url in self.start_urls:
            # yield SplashRequest(url, self.parse, endpoint='execute', args={'lua_source': load_page_script, 'wait': 3})
            yield SplashRequest(url, self.parse, args={'wait': 2})

    def parse(self, response):
        print("def parse")
        products = Selector(response).css(
            '.v-blog-wrap .v-blog-items-wrap .category-product .category-product-item')
        self.totalCrawled = self.totalCrawled + len(products)

        pages = {}
        for index, product in enumerate(products):
            item = {}
            urlProduct = product.css('a.product-image::attr(href)').get()
            arrSplitUrlProduct = urlProduct.split("/")
            arrSplitUrlProduct.insert(4, "nghe-truyen")
            urlProduct = "/".join(arrSplitUrlProduct)

            item['title'] = product.css('div.p-name h4 a::text').get().strip()
            item['href'] = urlProduct
            # Crawl detail
            yield SplashRequest(urlProduct, meta={'item': item, 'index': index}, callback=self.parse_detail, args={'wait': 0.5})
        # Check next page if exists
        next_page = response.css(
            '.dataTables_paginate ul.pagination li')[-2]
        next_page = next_page.css("a::attr(href)").get()
        if next_page is not None and next_page != 'javascript:void(0)':
            next_page = response.urljoin(next_page)
            print(next_page)
            yield response.follow(next_page, callback=self.parse)

    def parse_detail(self, response):
        item = response.request.meta['item']
        index = response.request.meta['index']
        product = Selector(response).css('article.portfolio-article')
        categoryName = (Selector(response).css(
            'div.v-page-heading ol.breadcrumb li:nth-child(3) a::text').get() or "none-category").strip()
        title = product.css('h1 a::text').get()
        img = product.css('figure.media-wrap a img::attr(src)').get()
        script = product.css(
            '#new-player > div > script:nth-child(1)::text').get()
        listUrlMp3 = [x.group() for x in re.finditer(
            r'(https?|ftp|file):\/\/(www.)?(.*?)\.(mp3)', script)]

        item["audio_resource"] = list(map(lambda link: link, listUrlMp3))
        item["img"] = img
        item["categoryName"] = categoryName
        self.dataCrawled = self.dataCrawled + 1
        print(">>>=======<<<<")
        print("{title} {categoryName} - index {index}".format(categoryName=categoryName, index=index, title=item["title"]))
        print("dataCrawled {dataCrawled} vs totalCrawled {totalCrawled}".format(dataCrawled=self.dataCrawled, totalCrawled=self.totalCrawled))
        print(">>>=======<<<<")
        yield item
