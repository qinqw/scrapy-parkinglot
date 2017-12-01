# -*- coding: utf-8 -*-
import scrapy
from parkingLot.items import ParkinglotProvinceItem


class ProvinceSpider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {
            'parkingLot.pipelines.JsonWriterProvincePipeline': 334
        }
    }
    name = 'province'
    allowed_domains = ['www.tingchewei.net']
    start_urls = ['http://www.tingchewei.net/']

    def parse(self, response):
        items = []
        item = ParkinglotProvinceItem()

        for sel in response.xpath('/html/body/div[1]/table[3]/tr/td'):
            for sel_2 in sel.xpath('div'):
                for sel_3 in sel_2.xpath('a'):
                    region = sel_2.xpath('strong/text()').extract()
                    name = sel_3.xpath('text()').extract()
                    url = sel_3.xpath('@href').extract()
                    province_code = ''.join(url).split('=')[1]
                    full_url = 'http://www.tingchewei.net/' + ''.join(url)

                    item['region'] = ''.join(region)
                    item['name'] = ''.join(name)
                    item['provinceCode'] = province_code
                    item['url'] = ''.join(url)
                    item['fullUrl'] = full_url

                    items.append(item)
                    yield item
                # region = sel.xpath('div/strong/text()').extract()
                # name = sel_2.xpath('a/text()').extract()
                # url = sel_2.xpath('a/@href').extract()
                # province_code = url
                # full_url = url

                # item['region'] = region 
                # item['name'] = name
                # item['provinceCode'] = province_code
                # item['url'] = url
                # item['fullUrl'] = full_url

                # items.append(item)
                # yield item