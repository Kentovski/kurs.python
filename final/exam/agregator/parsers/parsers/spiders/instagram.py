# -*- coding: utf-8 -*-
import scrapy
import json
from urllib.parse import urljoin


class InstagramSpider(scrapy.Spider):
    name = "instagram"
    allowed_domains = ["instagram.com"]

    def __init__(self, query=None, pages=3):
        self.pages = int(pages)
        self.start_urls = ['https://www.instagram.com/explore/tags/%s/?__a=1' % query]
        self.next_ = None
        self.has_next_page = None

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
                yield {
                        'direct_link': image['display_src'],
                        'source_link': urljoin('https://www.instagram.com/p/', image['code'])
                }
