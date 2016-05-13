from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from spiders.emailspider import EmailSpider

spider = EmailSpider()
spider.set_name('faircent')
spider.set_allowed_domains(['faircent.com'])
spider.set_start_urls('https://www.faircent.com/')

project_settings = Settings()
process = CrawlerProcess(project_settings)

process.crawl(spider)
process.start() # the script will block here until all crawling jobs are finished