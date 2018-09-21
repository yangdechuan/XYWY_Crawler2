# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class XywyCrawler2Pipeline(object):
    def open_spider(self, spider):
        host = "127.0.0.1"
        port = 27017
        dbname = "xywy"
        sheetname = "xywy_a"
        self.client = pymongo.MongoClient(host, port=port)
        self.mydb = self.client[dbname]
        self.post = self.mydb[sheetname]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = dict(item)
        self.post.save(data)

        return item