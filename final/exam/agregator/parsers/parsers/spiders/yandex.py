# -*- coding: utf-8 -*-
import scrapy
import json
from urllib.parse import urljoin


# run spider with command:
# scrapy crawl yandex -a query=your_query -a pages=3


class YandexSpider(scrapy.Spider):
    name = "yandex"

    def __init__(self, query=None, pages=3):
        pages = int(pages)
        self.start_urls = [
                'https://yandex.ua/images/search?text=%s&p=%s&rpt=image' % (query, page)
                for page in range(pages)
            ]

    def parse(self, response):
        images = response.xpath("//div[contains(@class, 'serp-item')]/@data-bem")
        for image in images:
            img = json.loads(image.extract())
            yield {
                    'direct_link': img['serp-item']['img_href'],
                    'source_link': img['serp-item']['snippet']['url']
            }
