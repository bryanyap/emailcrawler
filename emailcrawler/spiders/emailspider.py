import re
import tldextract

from items import EmailcrawlerItem
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import logging


class EmailSpider(CrawlSpider):
    name = ''
    item = EmailcrawlerItem()

    rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)

    def __init__(self, *args, **kwargs):
        super(EmailSpider, self).__init__(*args, **kwargs)

        self.name = kwargs.get('name')
        self.allowed_domains = list()
        self.start_urls = list()

        counter = 0
        with open(kwargs.get('filename')) as f:
            for line in f:
                if counter != 0:
                    if counter == kwargs.get('limit'):
                        break
                start_url = line.split('\t')[1]
                extracted = tldextract.extract(''.join(start_url.splitlines()))
                domain = "{}.{}".format(extracted.domain, extracted.suffix)

                counter += 1
                if not (start_url == None or domain == None or start_url == '' or domain == ''):
                    self.start_urls.append(start_url)
                    self.allowed_domains.append(domain)

    def parse_obj(self, response):
        logging.log(logging.INFO, 'Parsing: ' + str(response.url))
        domain = ''
        results = list()
        matches = re.findall(r'[\w\.-]+@[\w\.-]+', response.body)
        for match in matches:
            if match.split('@')[1] in self.allowed_domains:
                if domain == '':
                    domain = match.split('@')[1]
                if match not in results:
                    results.append(match)
        if len(results) > 0:
            item = EmailcrawlerItem()
            item['url'] = response.url
            item['emails'] = results
            item['domain'] = self.allowed_domains[0]
            return item
