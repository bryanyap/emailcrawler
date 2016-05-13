import os

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.emailspider import EmailSpider

# spider = EmailSpider(name='faircent', allowed_domain='faircent.com', start_url='https://www.faircent.com/')
# spider2 = EmailSpider(name='infocomminvestments', allowed_domain='infocomminvestments.com', start_url='http://www.infocomminvestments.com/')

try:
    os.remove('items.json')
except OSError:
    pass

process = CrawlerProcess(get_project_settings())

process.crawl(EmailSpider, name='faircent', allowed_domain='faircent.com', start_url='https://www.faircent.com/')
process.crawl(EmailSpider, name='infocomm investments', allowed_domain='infocomminvestments.com',
              start_url='http://www.infocomminvestments.com/')
process.start(stop_after_crawl=False)  # the script will block here until all crawling jobs are finished
