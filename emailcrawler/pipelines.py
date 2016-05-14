# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
import sqlite3

from scrapy import log


class EmailcrawlerPipeline(object):
    def __init__(self):
        self.file = open('items.json', 'a')

        os.remove('scrapedata.db')

        self.connection = sqlite3.connect('./scrapedata.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS scrape (domain VARCHAR(100), address VARCHAR(100), url VARCHAR(500), PRIMARY KEY(domain, address), FOREIGN KEY(address) REFERENCES emails.address)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS email (address VARCHAR(100), PRIMARY KEY(address))')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)

        emails = item['emails']
        for email in emails:
            self.cursor.execute("select * from email where address=?", email)
            result = self.cursor.fetchone()
            if not result:
                self.cursor.execute("insert into email (address) values (?)", email)
                self.cursor.execute("insert into scrape (domain, address, url) values (?,?,?)", item['domain'], email, item['url'])
                self.connection.commit()
                log.msg("Item stored : " % email, level=log.DEBUG)
            else:
                log.msg("Email already in database: %s" % email, level=log.DEBUG)
        return item
