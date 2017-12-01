# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ParkinglotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ParkinglotProvinceItem(scrapy.Item):
    region = scrapy.Field()
    name = scrapy.Field()
    provinceCode = scrapy.Field()
    url = scrapy.Field()
    fullUrl = scrapy.Field()

class ParkinglotCityItem(scrapy.Item):
    name = scrapy.Field()
    provinceCode = scrapy.Field()
    cityCode = scrapy.Field()
    url = scrapy.Field()
    fullUrl =  scrapy.Field()

class ParkinglotInfoListItem(scrapy.Item):
    url = scrapy.Field()

class ParkinglotInfoDetailItem(scrapy.Item):
    sid = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    category = scrapy.Field()
    district = scrapy.Field()
    contract = scrapy.Field()
    telphone = scrapy.Field()
    tencent_qq = scrapy.Field()
