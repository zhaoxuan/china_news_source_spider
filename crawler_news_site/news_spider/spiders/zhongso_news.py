#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright (C) 2016 John Zhao
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os
from urlparse import urlparse

import scrapy
from scrapy import signals

from news_spider.items import SpiderItem

origin_url = 'http://zixun.zhongsou.com/n?w=%s'
dir_path = os.path.dirname(os.path.realpath(__file__))
dicts_path = dir_path + '/../../../dicts.txt'


class ZhongsoNewsSpider(scrapy.Spider):
    name = 'zhongso_news_spider'
    allowed_domains = ['zhongsou.com']
    start_urls = []

    news_file = open(dicts_path, 'r')

    for word in news_file.readlines():
        start_urls.append(origin_url % word.strip())

    # 减慢爬取速度
    download_delay = 1

    def __init__(self):
        self.success = 0
        self.failure = 0

    # crawler 会调用这个方法创建 spider 实例
    # 所以在里面注册一个关闭的回调
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):

        spider = super(ZhongsoNewsSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.closed_handler, signals.spider_closed)

        return spider

    def closed_handler(self, spider):
        spider.logger.warning('ZhongsoNewsSpider closed, success: %d, failure: %d' % (self.success, self.failure))

    def parse(self, response):
        lists = response.xpath('//ul[@class="content-net-ul content-infor-ul"]/li')

        for item in lists:
            url = item.xpath('.//h3[@class="h3-zx"]/a/@href').extract()[0]
            name = item.xpath('.//div[@class="h3-wrap"]/font/nobr/text()').extract()[0]
            domain = urlparse(url).netloc
            spider_item = SpiderItem()
            spider_item['domain'] = domain
            spider_item['name'] = name.split()[0]

            yield spider_item
