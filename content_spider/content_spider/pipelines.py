# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        #email = tuple(sorted(item['email']))
        #phone = tuple(sorted(item['phone']))
        
        emails = list(item['email'])
        for email in emails:
            if email in self.ids_seen:
                item['email'].remove(email)
            else:
                self.ids_seen.add(email)
        
        phones = list(item['phone'])

        for phone in phones:
            if phone in self.ids_seen:
                item['phone'].remove(phone)
            else:
                self.ids_seen.add(phone) 
               
        return item  

class EmptyPipeline(object):


    def process_item(self, item, spider):
        
        if item['email'] == [] and item['phone'] == []:
            raise DropItem("Empty: %s" % item)
        else:
            return item  







class ContentSpiderPipeline(object):
    def process_item(self, item, spider):
        return item
