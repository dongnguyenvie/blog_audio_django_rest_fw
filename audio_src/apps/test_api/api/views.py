from rest_framework import generics
from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
# from audio_src.apps.crawls.crawls.spiders.stack_spider import StackSpider
# from scrapy.crawler import CrawlerProcess, Crawler, CrawlerRunner
import threading
import subprocess

def home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    loremText = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=json')
    response = {}
    response['id'] = ip
    response['lorem'] = loremText.text
    return JsonResponse(response, safe=False)
    
class TestView(viewsets.ViewSet):
    permission_classes = ()
    def dong(self, request):
        # def innerFnc():
            # process = CrawlerProcess(settings={
            #     'LOG_LEVEL': 'ERROR',
            #     # 'ITEM_PIPELINES': {
            #     #     'process_item': 300,
            #     # }
            # })
            # process.crawl(StackSpider)
            # process.start()

        # t = threading.Thread(target=innerFnc)
        # t.daemon = True
        # t.start()
        # subprocess.Popen(['cd', './scrapping'])
        subprocess.Popen(['ls'])
        # subprocess.Popen(['cd scrapping'])
        process = subprocess.Popen(['scrapy', 'crawl', 'stack'], cwd='scrapping')
        return JsonResponse({'method': 'get'}, safe=False)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

def process_item(self, item, spider):
    print(">>>>>>>================")
    print(item)
    print("====================<<<<<<<<<<<")
    return item