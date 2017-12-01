# -*- coding: utf-8 -*-
import scrapy
from parkingLot.items import ParkinglotInfoListItem


class InfolistSpider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {
            'parkingLot.pipelines.JsonWriterInfoListPipeline': 334
        }
    }
    name = 'infolist'
    allowed_domains = ['www.tingchewei.net']
    #start_urls = ['http://www.tingchewei.net/list.asp?city=5']
    start_urls = [
        'http://www.tingchewei.net/list.asp'
    ]

    def parse(self, response):
        items = []
        #print (response.xpath('/html/body/div[2]/table[3]/tr/td[1]/table[2]/tr[2]/td/table[2]').extract())
        #print(''.join(response.xpath('//td//a').extract()))
        print(''.join(response.xpath('//a[contains(.,"'+u'下一页'+'")]/@href').extract()))
        for sel in response.xpath('/html/body/div[2]/table[3]/tr/td[1]/table[2]/tr[2]/td/table[2]'):
            item = ParkinglotInfoListItem()
            # print(sel.xpath('tr/td[3]/a/@href').extract())
            url = sel.xpath('tr/td[3]/a/@href').extract()
            item['url'] = url
            items.append(item)
            yield item
        # 翻页
        next_page = response.xpath('//a[contains(.,"'+u'下一页'+'")]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            #爬每一页
            yield scrapy.Request(url, self.parse)
