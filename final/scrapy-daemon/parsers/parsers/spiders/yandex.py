# -*- coding: utf-8 -*-

import scrapy
import json
import datetime


# run spider with command:
# scrapy crawl yandex -a query=cat -a pages=3 -a django_task_id=1


class YandexSpider(scrapy.Spider):
    name = "yandex"

    def __init__(self, django_task_id, query=None, pages=3, *args, **kwargs):
        super(YandexSpider, self).__init__(*args, **kwargs)
        pages = int(pages)
        self.rank = 0
        self.django_task_id = django_task_id
        self.start_urls = [
                'https://yandex.ua/images/search?text=%s&p=%s&rpt=image' % (query, page)
                for page in range(pages)
            ]

    def parse(self, response):
        images = response.xpath("//div[contains(@class, 'serp-item')]/@data-bem")
        for image in images:
            img = json.loads(image.extract())
            self.rank += 1
            yield {
                    'django_task_id': self.django_task_id,
                    'direct_link': img['serp-item']['img_href'],
                    'source_link': img['serp-item']['snippet']['url'],
                    'rank': self.rank,
                    'site': 'y',
                    'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
