# -*- coding: utf-8 -*-
import scrapy
import json
import jsonpath
import time
import random
from CNN.items import CnnItem

def Link_Bulid(Link):
    temp = Link*100
    Link =Link+1
    Link = 'https://search.api.cnn.io/content?size=100&q=china&page=' + str(Link) \
           +'&from='+str(temp)#+'&category='+str(category)
    #Link = 'https://search.api.cnn.io/content?size=100&q=china%20trade%20war&page=' + str(Link) \
    #       + '&from=' + str(temp) #+ '&category=' + str(category)
    return Link

class CnnCrawlSpider(scrapy.Spider):
    name = 'CNN_Crawl'
    num=0
    #category='trade war'
    def start_requests(self):
        Link = Link_Bulid(self.num)
        yield scrapy.Request(url= Link,callback=self.parse,
                             meta={'num':self.num})

    def parse(self, response):
        if response.status == 200:
            text_data = json.loads(response.text)
            num=response.meta['num']
            item = CnnItem()
            for i in text_data['result']:
                item['Type'] = jsonpath.jsonpath(i,'$..type')
                item['Url'] = jsonpath.jsonpath(i, '$..url')
                item['Source'] = jsonpath.jsonpath(i, '$..source')
                try:
                    item['Location'] = jsonpath.jsonpath(i, '$..location')
                except:
                    item['Location'] =''
                try:
                    item['ByLine'] = jsonpath.jsonpath(i, '$..byLine')
                except:
                    item['ByLine'] =''
                item['Writers'] = jsonpath.jsonpath(i, '$..contributors')
                item['FirstPublishDate'] = jsonpath.jsonpath(i, '$..firstPublishDate')
                item['LastModifiedDate'] = jsonpath.jsonpath(i, '$..lastModifiedDate')
                item['Headline'] = jsonpath.jsonpath(i, '$..headline')
                item['Section'] = jsonpath.jsonpath(i, '$..section')
                item['MappedSection'] = jsonpath.jsonpath(i, '$..mappedSection')
                item['Article_Body'] = jsonpath.jsonpath(i, '$..body')
                item['Language'] = jsonpath.jsonpath(i, '$..language')
                yield item
            #text_data['meta']['of']
            if 5800>(num*100):
                num += 1
                Link = Link_Bulid(num)
                yield scrapy.Request(url=Link, callback=self.parse,
                                     meta={'num': num})