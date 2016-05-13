from scrapy.crawler import CrawlerProcess
from spiders.emailspider import EmailSpider

process = CrawlerProcess()
process.crawl(EmailSpider)
process.start() # the script will block here until all crawling jobs are finished