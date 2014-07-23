# -*- coding: utf-8 -*-

# Scrapy settings for content_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'content_spider'
DEPTH_LIMIT = 1
SPIDER_MODULES = ['content_spider.spiders']
NEWSPIDER_MODULE = 'content_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'content_spider (+http://www.yourdomain.com)'
