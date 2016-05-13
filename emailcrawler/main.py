import os

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.emailspider import EmailSpider
<<<<<<< HEAD
import os
import tldextract
=======

# spider = EmailSpider(name='faircent', allowed_domain='faircent.com', start_url='https://www.faircent.com/')
# spider2 = EmailSpider(name='infocomminvestments', allowed_domain='infocomminvestments.com', start_url='http://www.infocomminvestments.com/')
>>>>>>> 7470ff9fd4abe110269f54b103a4066f55ccc4dd

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

<<<<<<< HEAD
process.start(stop_after_crawl=True) # the script will block here until all crawling jobs are finished
=======
process.crawl(EmailSpider, name='faircent', allowed_domain='faircent.com', start_url='https://www.faircent.com/')
process.crawl(EmailSpider, name='infocomm investments', allowed_domain='infocomminvestments.com',
              start_url='http://www.infocomminvestments.com/')
process.start(stop_after_crawl=False)  # the script will block here until all crawling jobs are finished
>>>>>>> 7470ff9fd4abe110269f54b103a4066f55ccc4dd
