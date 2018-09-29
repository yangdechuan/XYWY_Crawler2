# -*- coding: utf-8 -*-
import os
import re
import scrapy

from XYWY_Crawler2.items import XywyCrawler2Item


class XywySpiderSpider(scrapy.Spider):
    name = 'xywy_spider'
    allowed_domains = ['club.xywy.com']
    start_urls = ['http://club.xywy.com/']

    def start_requests(self):
        filenames = os.listdir("urls")
        for filename in filenames:
            if re.match("xywy_qa_urls", filename) is None:
                continue
            urls = []
            with open(os.path.join("urls", filename), "r") as fr:
                for line in fr.readlines():
                    urls.append(line.strip())
            for url in urls:
                yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # question = response.xpath("//div[@class='User_askcon clearfix pr']//div[@class='graydeep User_quecol pt10 mt10']/text()").extract_first()
        answers = response.xpath("//div[@class='docall clearfix ']//div[@class='pt15 f14 graydeep  pl20 pr20 deepblue']/text()").extract()
        url = response.url
        _id = url.split("/")[-1].replace(".htm", "")

        item = XywyCrawler2Item()
        item["_id"] = _id
        item["answers"] = answers

        yield item