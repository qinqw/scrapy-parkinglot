# -*- coding: utf-8 -*-
import scrapy


class CitySpider(scrapy.Spider):
    name = 'city'
    allowed_domains = ['www.tingchewei.net']
    start_urls = ['http://www.tingchewei.net/']

    def parse(self, response):
        pass
