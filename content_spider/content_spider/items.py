# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ContentSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    phone = Field()
    url = Field()
    email = Field()
    tag = Field()
