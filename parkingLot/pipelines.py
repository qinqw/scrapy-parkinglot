# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import MySQLdb
import MySQLdb.cursors

class ParkinglotPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWriterProvincePipeline(object):
    def __init__(self):
        self.file = codecs.open('rgion_province.json', 'wb', 'utf-8')

    def process_item(self, item, spider):
        rep_item = item
        #print(spider.name)
        line = json.dumps(dict(rep_item), ensure_ascii=False).replace('\n', '')
        self.file.write(line.replace(' ', '') + "\n")
        return item

class JsonWriterCityPipeline(object):
    def __init__(self):
        self.file = open('region_city.json', 'wb' )

    def process_item(self, item, spider):
        rep_item = item
        line = json.dumps(dict(rep_item)).replace('\n', '')
        self.file.write(line.replace(' ', '') + "\n")
        return item

class JsonWriterInfoListPipeline(object):
    def __init__(self):
        self.file = codecs.open('infolist.json', 'wb', 'utf-8')

    def process_item(self, item, spider):
        rep_item = item
        line = json.dumps(dict(rep_item), ensure_ascii=False).replace('\n', '')
        self.file.write(line.replace(' ', '') + "\n")
        return item

class JsonWriterInfoDetailPipeline(object):
    def __init__(self):
        self.file = codecs.open('infoDetail.json', 'wb', 'utf-8')

    def process_item(self, item, spider):
        rep_item = item
        line = json.dumps(dict(rep_item), ensure_ascii=False).replace('\n', '')
        self.file.write(line.replace(' ', '') + "\n")
        return item

# CREATE TABLE `analysis`.`chewei_info_detail` (
#   `id` INT NOT NULL AUTO_INCREMENT,
#   `sid` VARCHAR(45) NULL,
#   `title` VARCHAR(500) NULL,
#   `date` VARCHAR(45) NULL,
#   `category` VARCHAR(45) NULL,
#   `district` VARCHAR(45) NULL,
#   `contract` VARCHAR(45) NULL,
#   `telphone` VARCHAR(45) NULL,
#   `tencent_qq` VARCHAR(45) NULL,
#   `create_time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
#   `update_time` TIMESTAMP NULL ON UPDATE CURRENT_TIMESTAMP(),
#   PRIMARY KEY (`id`));
class MysqldbInfoDetailPipeline(object):
    def __init__(self):
        # 打开数据库连接
        self.conn = MySQLdb.connect(host="localhost",user="root",passwd="root",db="analysis",charset="utf8")
        self.cursor = self.conn.cursor()
        # # 清空表
        # self.cursor.execute('truncate table chewei_info_detail;')
        # self.conn.commit()

    def process_item(self, item, spider):
        sid = item['sid']
        title = item['title']
        date = item['date']
        category = item['category']
        district = item['district']
        contract = item['contract']
        telphone = item['telphone']
        tencent_qq = item['tencent_qq']
        row_nums = self.cursor.execute("""select * from chewei_info_detail where sid="""+sid)
        #self.conn.commit()
        if row_nums == 0 :
            self.cursor.execute("""
                    insert IGNORE into chewei_info_detail(sid, title, date, category, district, contract, telphone, tencent_qq)
                    values(%s, %s, %s, %s, %s, %s, %s, %s)
                    """, (sid, title, date, category, district, contract, telphone, tencent_qq))
            self.conn.commit()
        return item