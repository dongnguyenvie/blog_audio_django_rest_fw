# file spider.py
from urllib.parse import urljoin
import re
import json
import threading
import requests
from bs4 import BeautifulSoup


class Spider:

    # Class variables (shared among all instances)
    q = None
    base_url = 'https://archive.org/download/'

    def __init__(self, onJob):
        Spider.q = onJob
        self._create_spiders()

    def _work(self):
        while True:
            [model, id_target] = self.q.get()
            result = self.crawl_archive(
                threading.currentThread().name, id_target)
            model.resource = json.dumps(result)
            model.save()
            self.q.task_done()

    def _create_spiders(self):
        t = threading.Thread(target=self._work)
        t.daemon = True
        t.start()

    @staticmethod
    def crawl_archive(thread_name, id_targets):
        print(thread_name + ' now crawling ' + id_targets)
        results = []
        if isinstance(id_targets, str):
            list_id_target = id_targets.split(",")
            for id_target in list_id_target:
                results += Spider.crawling(id_target)
            results.sort(key=sort_archive)
        return results

    @staticmethod
    def crawling(id_target):
        results = []
        url_target = urljoin(Spider.base_url, id_target)
        content = requests.get(url_target)
        soup = BeautifulSoup(content.text, 'html.parser')
        for elem in soup.select("table.directory-listing-table tbody td a", href=True):
            link = elem.get("href")
            text = elem.getText()
            if link.endswith(".mp3"):
                results.append({text: urljoin(url_target, link)})
        return results

    @staticmethod
    def create_archive_crawl_jobs(model, id_target):
        Spider.q.put([model, id_target])
        # Spider.q.join() # await for job end


def sort_archive(obj):
    [arr_val] = [v for v in obj.values()]
    arr_number = re.findall('[0-9]+', arr_val)
    val = int("".join(arr_number))
    return val
