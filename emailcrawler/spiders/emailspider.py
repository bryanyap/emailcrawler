from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from items import EmailcrawlerItem
import re

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
        matches = re.findall(r'[\w\.-]+@[\w\.-]+', response.body)
        emails = list()
        for match in matches:
            if match not in emails:
                emails.append(match)
        if len(emails) > 0:
            item = EmailcrawlerItem()  
            item['url'] = response.url
            item['emails'] = emails
            return item

