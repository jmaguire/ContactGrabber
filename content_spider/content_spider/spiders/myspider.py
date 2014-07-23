
from scrapy.selector import HtmlXPathSelector
from content_spider.items import ContentSpiderItem
from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.selector import Selector
from bs4 import BeautifulSoup
from scrapy.contrib.linkextractors import LinkExtractor
import os
import re
import json
from scrapy.conf import settings

def getJSONData(filename):
    with open(filename) as readfile:
        data = json.load(readfile)
    return data    

class MySpider(CrawlSpider):
    path = os.path.dirname(os.path.abspath(__file__))
    #url = 'mountainview.gov'
    name = "monkey"
    #allowed_domains = [url]
    #start_urls = ['http://' + url]
    allowed_domains = getJSONData(path + '/urls.json'); #[elem.encode('ascii', errors ='ignore') for elem in getJSONData(path + '/urls.json')]
    start_urls = ['http://www.' + elem for elem in allowed_domains] #getJSONData(path + '/urls.json')
    print allowed_domains
    print start_urls

    rules = (
        Rule(LinkExtractor(allow_domains=allowed_domains), callback = 'parse_items',follow ="True"),
    )
    
        

    def __init__(self, name = None, **kwargs):
        super(MySpider, self).__init__()
        self.whitelist = getJSONData(MySpider.path + '/whitelist.json')

    def checkWhitelist(self, string):
        string = string.lower()
        for item in self.whitelist:
            if item in string:
                return item
        return None

    def parse_items(self, response):
        soup = BeautifulSoup(response.body)
        #sel = Selector(response)
        html = self.decodeUnicode(response.body);
        tag = self.checkWhitelist(html)
        if tag is None:
            return []
        
        texts = [self.decodeUnicode(elem) for elem in soup.findAll(text = True)]
        texts = [elem for elem in texts if len(elem) > 0]
        #print texts
        #text = self.decodeUnicode(' '.join(sel.xpath('//p/text()').extract()))
        #possible_emails = self.decodeUnicode(' '.join(sel.xpath('//a/@href').extract()))
        
        emails = [link['href'] for link in soup.findAll("a") 
                            if link.has_attr('href') and self.isEmail(link['href'])]
        emails = [email.replace('mailto:','') for email in emails]
        #phones = [elem for elem in texts 
        #                    if self.isPhone(elem)]
        #print emails
        #print phones
        #emails = self.getEmailAddress(possible_emails)
        phones = self.getPhoneNumbers(' '.join(texts))
        item = ContentSpiderItem()
        #if len(phones) > 3 or len(emails) > 3:
        item['phone'] = phones
        item['url'] = response.url
        item['email'] = emails
        item['tag'] = tag
        return item
    
    def isEmail(self, string):
        return re.findall(r'[\w\.-]+@[\w\.-]+', string) != []

    def isPhone(self, string):
        return re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',string) != []

    def decodeUnicode(self, string):
        try:
            return re.sub('\s+',' ', string).encode('ascii', errors ='ignore').strip()
        except:
            return ""
    def getEmailAddress(self, string):
        return re.findall(r'[\w\.-]+@[\w\.-]+', string)

    def getPhoneNumbers(self, string):
        return re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',string)
