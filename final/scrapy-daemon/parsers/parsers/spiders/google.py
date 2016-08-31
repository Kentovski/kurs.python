# -*- coding: utf-8 -*-

import scrapy
from urlparse import urljoin
import datetime

# run spider with command:
# scrapy crawl google -a query=cat -a pages=3 -a django_task_id=1


class GoogleSpider(scrapy.Spider):
    name = "google"

    def __init__(self, django_task_id, query=None, pages=3, *args, **kwargs):
        super(GoogleSpider, self).__init__(*args, **kwargs)
        pages = int(pages)
        self.rank = 0
        self.django_task_id = django_task_id
        self.start_urls = [
                'https://www.google.com.ua/search?tbm=isch&q=%s&start=%s&gws_rd=ssl' % (query, page * 10)
                for page in range(pages)
            ]

    def parse(self, response):
        for link, _ in enumerate(response.xpath('//table[@class="images_table"]//img/@src').extract()):
            full_url = urljoin('http://google.com.ua', response.xpath('//table[@class="images_table"]//td/a/@href').extract()[link])
            request = scrapy.Request(full_url, callback=self.go_redirect)
            request.meta['direct_link'] = response.xpath('//table[@class="images_table"]//img/@src').extract()[link]
            yield request

    def go_redirect(self, response):
        self.rank += 1
        yield {
            'django_task_id': self.django_task_id,
            'source_link': response.request.url,
            'direct_link': response.meta['direct_link'],
            'rank': self.rank,
            'site': 'g',
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
