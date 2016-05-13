import os

import tldextract
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.emailspider import EmailSpider

try:
    os.remove('items.json')
except OSError:
    pass

process = CrawlerProcess(get_project_settings())
counter = 0

with open('/home/bryan/Desktop/tia_selected_websites.csv') as f:
    for line in f:
        if counter == 50:
            break
        start_url = line.split('\t')[1]
        name = line.split('\t')[0]

        extracted = tldextract.extract(''.join(start_url.splitlines()))
        allowed_domain = "{}.{}".format(extracted.domain, extracted.suffix)

        process.crawl(EmailSpider, name=name, allowed_domain=allowed_domain, start_url=start_url)
        counter += 1

process.start(stop_after_crawl=True)  # the script will block here until all crawling jobs are finished
