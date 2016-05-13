import re

from items import EmailcrawlerItem
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class EmailSpider(CrawlSpider):
    name = ''
    item = EmailcrawlerItem()

    rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)

    def __init__(self, *args, **kwargs):
        super(EmailSpider, self).__init__(*args, **kwargs)

        self.name = kwargs.get('name')
        self.allowed_domains = [kwargs.get('allowed_domain')]
        self.start_urls = [kwargs.get('start_url')]

    def parse_obj(self, response):
        results = list()
        matches = re.findall(r'[\w\.-]+@[\w\.-]+', response.body)
        for match in matches:
            if match.split('@')[1] == self.allowed_domains[0]:
                if match not in results:
                    results.append(match)
        if len(results) > 0:
            item = EmailcrawlerItem()
            item['url'] = response.url
            item['emails'] = results
            return item
