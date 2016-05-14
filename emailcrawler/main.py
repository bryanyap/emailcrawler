import os
from sys import argv

import tldextract
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.emailspider import EmailSpider

if len(argv) != 3:
    raise ValueError('Please key in the correct number of inputs')

try:
    input_number = int(argv[1])
except:
    raise ValueError('Please key in an integer value')

try:
    filename = argv[2]
    open(argv[2])
except:
    raise ValueError('Please key in a correct file input')

try:
    os.remove('scrapedata.db')
except:
    pass

process = CrawlerProcess(get_project_settings())

start_urls = list()
name = 'emailcrawler'

process.crawl(EmailSpider, name=name, filename=filename, limit=input_number)
process.start(stop_after_crawl=True)  # the script will block here until all crawling jobs are finished
