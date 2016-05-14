# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import logging


class EmailcrawlerPipeline(object):
    def __init__(self):
        self.connection = sqlite3.connect('scrapedata.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS email (address VARCHAR(100), PRIMARY KEY(address))')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS scrape (domain VARCHAR(100), address VARCHAR(100), url VARCHAR(500), PRIMARY KEY(domain, address), FOREIGN KEY(address) REFERENCES emails(address))')
        self.connection.commit()

    def process_item(self, item, spider):
        for email in item['emails']:
            self.cursor.execute('select * from email where address=\'' + str(email) + '\'')
            result = self.cursor.fetchone()
            if not result:
                self.cursor.execute('insert into email (address) values (\'' + str(email) + '\')')
                self.cursor.execute('insert into scrape (domain, address, url) values (' + '\'' + str(item['domain']) + '\'' +',\'' + str(email) + '\'' +  ',\'' + item['url'] + '\'' + ')')
                self.connection.commit()
                logging.log(logging.INFO, 'Item stored : ' +  str(email))
            else:
                logging.log(logging.INFO, 'Email already in database: ' + str(email))
        return item
