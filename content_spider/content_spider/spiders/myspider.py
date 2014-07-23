
from scrapy.selector import HtmlXPathSelector
from content_spider.items import ContentSpiderItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors import LinkExtractor

import re

from scrapy.conf import settings

class MySpider(CrawlSpider):
    name = "monkey"
    allowed_domains = ["cityofoberlin.com"]
    start_urls = ["http://www.cityofoberlin.com"]
    rules = (
        Rule(LinkExtractor(allow_domains=["cityofoberlin.com"]), callback = 'parse_items',follow ="True"),
    )
    
    def parse_items(self, response):
        sel = HtmlXPathSelector(response)
        text = self.decodeUnicode(' '.join(sel.xpath('//p/text()').extract()))
        phones = self.getPhoneNumbers(text)
        item = ContentSpiderItem()

        if len(phones) > 3:
            item['phone'] = phones
            item['url'] = response.url
        return item
        
    def decodeUnicode(self, string):
        return re.sub('\s+',' ', string).encode('ascii', errors ='ignore').strip()

    def getEmailAddress(self, string):
        return re.findall(r'[\w\.-]+@[\w\.-]+', string)

    def getPhoneNumbers(self, string):
        return re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',string)
