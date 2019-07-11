# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CnnItem(scrapy.Item):
    Type = scrapy.Field()
    Url = scrapy.Field()
    Source = scrapy.Field()
    Location = scrapy.Field()
    ByLine = scrapy.Field()
    Writers = scrapy.Field()
    FirstPublishDate = scrapy.Field()
    LastModifiedDate = scrapy.Field()
    Headline = scrapy.Field()
    Section = scrapy.Field()
    MappedSection = scrapy.Field()
    Article_Body = scrapy.Field()
    Language = scrapy.Field()
