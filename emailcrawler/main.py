import os
from sys import argv

import tldextract
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.emailspider import EmailSpider

if len(argv) != 2:
    raise ValueError('Please key in the correct number of inputs')

try:
    input_number = int(argv[1])
except:
    raise ValueError('Please key in an integer value')

try:
    os.remove('items.json')
except OSError:
    pass

try:
    os.remove('scrapedata.db')
except:
    pass

process = CrawlerProcess(get_project_settings())
counter = 0

with open('/home/bryan/Desktop/tia_selected_websites.csv') as f:
    for line in f:
        if counter == 0:
            if counter == input_number:
                break
        start_url = line.split('\t')[1]
        name = line.split('\t')[0]

        extracted = tldextract.extract(''.join(start_url.splitlines()))
        allowed_domain = "{}.{}".format(extracted.domain, extracted.suffix)

        process.crawl(EmailSpider, name=name, allowed_domain=allowed_domain, start_url=start_url)
        counter += 1

process.start(stop_after_crawl=True)  # the script will block here until all crawling jobs are finished
