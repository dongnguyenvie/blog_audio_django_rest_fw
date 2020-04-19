# file spider.py
from urllib.parse import urljoin
import re
import requests
from bs4 import BeautifulSoup
# from commons.crawler.domain import get_domain_name


class Spider:

    # Class variables (shared among all instances)
    domain_name = ''
    base_url = 'https://archive.org/download/'
    queue = set()
    crawled = set()

    def __init__(self, domain_name, base_url):
        Spider.domain_name = domain_name
        Spider.base_url = base_url
        Spider.queue.add(base_url)
        # self.crawl_page('First spider', Spider.base_url)

    # @staticmethod
    # def crawl_page(thread_name, page_url):
    #     # if page_url not in Spider.crawled:
    #     print(thread_name + ' now crawling ' + page_url)
    #     print('Queue ' + str(len(Spider.queue)) + ' | ' +
    #           'Crawled ' + str(len(Spider.crawled)))
    #     return Spider.gather_links(page_url)
    #     # Spider.add_links_to_queue(Spider.gather_links(page_url))
    #     # Spider.queue.remove(page_url)
    #     # Spider.crawled.add(page_url)

    # @staticmethod
    # def gather_links(page_url):
    #     results = set()
    #     content = requests.get(page_url)
    #     soup = BeautifulSoup(content.text, 'html.parser')

    #     for elem in soup.find_all("a", href=True):
    #         link = urljoin(page_url, elem['href'])
    #         results.add(link)
    #     return results

    # @staticmethod
    # def add_links_to_queue(links):
    #     for url in links:
    #         if (url in Spider.queue) or (url in Spider.crawled):
    #             continue
    #         if Spider.domain_name != get_domain_name(url):
    #             continue
    #         Spider.queue.add(url)

    @staticmethod
    def crawl_archive(id_target):
        results = []
        url_target = urljoin(Spider.base_url, id_target)
        content = requests.get(url_target)
        soup = BeautifulSoup(content.text, 'html.parser')
        for elem in soup.select("table.directory-listing-table tbody td a", href=True):
            link = elem.get("href")
            text = elem.getText()
            if link.endswith(".mp3"):
                results.append({text: urljoin(url_target, link)})
        results.sort(key=sort_archive)
        return results


def sort_archive(obj):
    [arr_val] = [v for v in obj.values()]
    arr_number = re.findall('[0-9]+', arr_val)
    val = int("".join(arr_number))
    return val
