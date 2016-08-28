# -*- coding: utf-8 -*-

import scrapy
from urllib.parse import urljoin
from scrapy.loader import ItemLoader
from parsers.items import GoogleItem
# from scrapy.shell import inspect_response

# run spider with command:
# scrapy crawl google -a query=your_query -a pages=3


class GoogleSpider(scrapy.Spider):
    name = "google"

    def __init__(self, query=None, pages=3):
        pages = int(pages)
        self.start_urls = [
                'https://www.google.com.ua/search?tbm=isch&q=%s&start=%s&gws_rd=ssl' % (query, page * 10)
                for page in range(pages)
            ]

    def parse(self, response):

        for link, _ in enumerate(response.xpath('//table[@class="images_table"]//img/@src').extract()):
            full_url = urljoin('http://google.com.ua', response.xpath('//table[@class="images_table"]//td/a/@href').extract()[link])
            request = scrapy.Request(full_url, callback=self.go_redirect)
            request.meta['direct_link'] = response.xpath('//table[@class="images_table"]//img/@src').extract()[link]
            yield  request


    def go_redirect(self, response):
        f = ItemLoader(item=GoogleItem())
        direct_link = response.meta['direct_link']
        f.add_value('source_link', response.request.url)
        f.add_value('direct_link', direct_link)
        return f.load_item()
