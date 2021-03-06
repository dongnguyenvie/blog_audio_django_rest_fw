import json
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
import csv
from django.conf import settings  # correct way
from audio_src.apps.articles.models import Article
import math
import random
import uuid

base_dir = settings.BASE_DIR

contentSeed = """
<p>Lâm Nhược Trần ngồi ở mép giường cúi đầu không nói, Mạc Vấn đứng ở bên cạnh bàn nhìn khay gỗ trên bàn sơn đỏ, trong khay gỗ là hai kiện khí vật, một là cây gậy như ý** bằng gỗ tùng khắc hình đồng nam đồng nữ, cái kia là một cây hỉ xứng ** có khắc hai ngôi sao Bắc Đẩu Nam Đẩu. Chú rể nếu dùng tay không vén khăn cô dâu sẽ bị cho là xui xẻo, phải dùng gậy như ý hoặc hỉ xứng đẩy lên, còn dúng cái nào thì tuỳ theo sở thích.<br>
audio vyvy xin giới thiệu Truyện tiên hiệp Tử Dương [mp3]</p>
"""
excerptText = """
Vestibulum ac diam sit amet quam vehicula elementum sed sit amet dui. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. Cras ultricies ligula sed magna dictum porta. Sed porttitor lectus nibh. Vivamus suscipit tortor eget felis porttitor volutpat. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Donec sollicitudin molestie malesuada. Pellentesque in ipsum id orci porta dapibus. Vivamus suscipit tortor eget felis porttitor volutpat. Donec sollicitudin molestie malesuada.
"""
thumbnailSeed = "https://picsum.photos/450/675"


def home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    loremText = requests.get(
        'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=json')
    response = {}
    response['id'] = ip
    response['lorem'] = loremText.text
    return JsonResponse(response, safe=False)


token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk3MjUyOTMxLCJqdGkiOiJiM2ZkNjIwNmNmZTk0ZDczOTllNDkxZmIyNjM3Y2JjZiIsInVzZXJfaWQiOiIwMTU5ZDlhZi1lMDEyLTRmYzQtOWRhNC00ZmUzYzNkODczM2IifQ.VmOjPapMIDXusx2tr0iJUkfnh0MEa657foQSwMdZurw'


class TestView(viewsets.ViewSet):
    permission_classes = []
    authentication_classes = []

    def dong(self, request):
        subprocess.Popen(['ls'])
        process = subprocess.Popen(
            ['scrapy', 'crawl', 'TruyenaudioSpider', '-o', 'data/data-raw.csv'], cwd='scrapping')
        return JsonResponse({'method': 'get'}, safe=False)

    def importSeedData(self, request):
        data = []
        with open(base_dir + '/scrapping/data/data-raw.csv', 'r', encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                elif line_count > 600 and line_count < 650:
                    url = 'http://localhost:8000/api/v1/article/'
                    headers = {
                        'authorization': 'Bearer {token}'.format(token=token),
                        'Content-Type': 'application/json'
                    }
                    # resource = map(lambda x: {'url': x},
                    #                list(row[2].split(",")))
                    resource = map(
                        lambda x: {'url': x, 'title': None}, list(row[2].split(",")))
                    # print(json.dumps(list(resource)))
                    data = {
                        'resource': json.dumps(list(resource)),
                        'content': contentSeed,
                        'excerpt': excerptText,
                        'thumbnail': row[3],
                        "title": row[0],
                        "slug": "slug-of-{uuid}".format(uuid=uuid.uuid4()),
                        "ping": False,
                        "type": 3,
                        'meta': {
                                'jsonLd': "",
                                'view': math.ceil(random.random() * 100),
                                'like': math.ceil(random.random() * 100),
                        },
                        'categories': ['8ec542ae-f651-49bd-bd08-c850f4c3e7c9'],
                        'tags': ['52d9bd03-bbae-475c-afe5-183e17419648']
                    }
                    try:
                        response = requests.post(
                            url, json=data, headers=headers)
                        response.raise_for_status()
                    except requests.exceptions.HTTPError as e:
                        print(e.response.text)

                    # post = Post(title=row[0], slug=row[1], source=json.dumps(row[2].split(
                    #     ",")), content=contentSeed, excerpt=excerptText, thumbnail=thumbnailSeed)
                    # post.save()
                line_count += 1

        return JsonResponse({'message': 'succses'}, safe=False)

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
