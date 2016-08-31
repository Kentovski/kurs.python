# -*- coding: utf-8 -*-

import scrapy
import json
from urlparse import urljoin
import datetime

# run spider with command:
# scrapy crawl instagram -a query=cat -a pages=2 -a django_task_id=1

class InstagramSpider(scrapy.Spider):
    name = "instagram"
    allowed_domains = ["instagram.com"]

    def __init__(self, django_task_id, query=None, pages=3, *args, **kwargs):
        super(InstagramSpider, self).__init__(*args, **kwargs)
        self.pages = int(pages)
        self.start_urls = ['https://www.instagram.com/explore/tags/%s/?__a=1' % query]
        self.next_ = None
        self.rank = 0
        self.has_next_page = None
        self.django_task_id = django_task_id

    def parse(self, response):
        while True:
            if self.pages <= 0:
                break
            if self.next_ is None:
                api = json.loads(response.body_as_unicode())
                next_ = api['tag']['media']['page_info']['end_cursor']
                has_next_page = api['tag']['media']['page_info']['has_next_page']
            else:
                next_ = self.next_
                has_next_page = self.has_next_page
            if has_next_page:
                next_link = urljoin(response.url, '?__a=1&max_id=%s' % next_)
                yield scrapy.Request(next_link, callback=self.get_page)

    def get_page(self, response):
        api = json.loads(response.body_as_unicode())
        self.next_ = api['tag']['media']['page_info']['end_cursor']
        self.has_next_page = api['tag']['media']['page_info']['has_next_page']
        images = api['tag']['media']['nodes']
        self.pages -= 1
        for image in images:
            if not image['is_video']:
                self.rank += 1
                yield {
                        'django_task_id': self.django_task_id,
                        'direct_link': image['display_src'],
                        'source_link': urljoin('https://www.instagram.com/p/', image['code']),
                        'rank': self.rank,
                        'site': 'i',
                        'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
