# -*- coding: utf-8 -*-
import re
import scrapy
from parkingLot.items import ParkinglotInfoDetailItem

class InfodetailSpider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {
            'parkingLot.pipelines.JsonWriterInfoDetailPipeline': 334,
            'parkingLot.pipelines.MysqldbInfoDetailPipeline': 500
        }
    }
    name = 'infodetail'
    allowed_domains = ['www.tingchewei.net']
    start_urls = ['http://www.tingchewei.net/view.asp?id=9587&city=2']

    def start_requests(self):
        url = 'http://www.tingchewei.net/view.asp?id=9587&city=2'
        # 如果 self.tag 存在返回 tag 本身的值，不存在返回 None
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = 'http://www.tingchewei.net/' + tag
        # 把构建好的 url 用 parse() 方法处理
        yield scrapy.Request(url, self.parse)


    def parse(self, response):
        items = []
        #for sel in response.xpath('/html/body/div[2]/table[3]/tr/td[1]/table[2]/tr[2]/td/table[2]'):
        item = ParkinglotInfoDetailItem()
        # print(sel.xpath('tr/td[3]/a/@href').extract())
        # /html/body/div[2]/table[2]/tr/td[1]/table[2]/tr[2]/td/table[1]
        sel_root = response.xpath('/html/body/div[2]/table[2]/tr/td[1]/table[2]/tr[2]/td/table[1]')
        #/tr[2]/td/a/@href
        #title = response.xpath('/html/body/div[2]/table[2]/tr/td[1]/table[2]/tr[2]/td/table[1]/tr[1]/td/h1/text()').extract()
        fav_url = sel_root.xpath('tr[2]/td/a/@href').extract()
        sid = re.findall(r"id=(.+?)&title", ''.join(fav_url))
        title = sel_root.xpath('tr[1]/td/h1/text()').extract()
        date_field = sel_root.xpath('tr[2]/td/text()').extract()
        date = re.findall(u"发布时间：(.+?) \xa0\xa0浏览次数：", ''.join(date_field))
        category = sel_root.xpath('tr[3]/td[2]/text()').extract()
        district = sel_root.xpath('tr[4]/td[2]/text()').extract()
        contract = sel_root.xpath('tr[5]/td[2]/text()').extract()
        telphone = sel_root.xpath('tr[8]/td[2]/text()').extract()
        tencent_qq = sel_root.xpath('tr[9]/td[2]/text()').extract()
        item['sid'] = ''.join(sid).encode('raw_unicode_escape')
        item['title'] = ''.join(title)
        item['date'] = ''.join(date).encode('raw_unicode_escape')
        item['category'] = ''.join(category)
        item['district'] = ''.join(district)
        item['contract'] = ''.join(contract)
        item['telphone'] = ''.join(telphone)
        item['tencent_qq'] = ''.join(tencent_qq)
        items.append(item)
        yield item
