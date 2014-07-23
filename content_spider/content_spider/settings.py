# -*- coding: utf-8 -*-

# Scrapy settings for content_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'content_spider'
DEPTH_LIMIT = 2
SPIDER_MODULES = ['content_spider.spiders']
NEWSPIDER_MODULE = 'content_spider.spiders'
LOG_ENABLED = False
COOKIES_ENABLED = False
ITEM_PIPELINES = {
    'content_spider.pipelines.DuplicatesPipeline': 10,
    'content_spider.pipelines.EmptyPipeline': 20
}
USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'content_spider (+http://www.yourdomain.com)'


