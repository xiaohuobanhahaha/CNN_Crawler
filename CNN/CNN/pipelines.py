# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class CnnPipeline(object):
    def open_spider(self,spider):
        self.out = open("CNN-china.csv", "w")
        self.writer = csv.writer(self.out)
        self.writer.writerow(['Type','Url', 'Source','Location', 'ByLine','Writers','FirstPublishDate',
                     'LastModifiedDate', 'Headline','Section', 'MappedSection','Article_Body',
                     'Language'])
    def process_item(self, item, spider):
        self.writer.writerow([item['Type'],item['Url'], item['Source'],item['Location'],
                    item['ByLine'],item['Writers'],item['FirstPublishDate'],
                    item['LastModifiedDate'], item['Headline'],item['Section'],
                    item['MappedSection'],item['Article_Body'],item['Language']])
        return item
    def close_spider(self,spider):
        self.out.close()