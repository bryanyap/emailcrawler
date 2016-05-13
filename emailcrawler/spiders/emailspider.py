from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from emailcrawler.items import EmailcrawlerItem


class EmailSpider(CrawlSpider):
    name = "faircent"
    allowed_domains = ["faircent.com"]
    start_urls = ["https://www.faircent.com/"]
    item = EmailcrawlerItem()

    rules = (Rule(LxmlLinkExtractor(allow=()), callback='parse_obj', follow=True),)

    def parse_obj(self, response):
        for link in LxmlLinkExtractor(allow=(), deny=self.allowed_domains).extract_links(response):
            item = EmailcrawlerItem()
            item['url'] = link.url
            yield

    def set_allowed_domains(self, allowed_domains):
        self.allowed_domains = allowed_domains

    def set_name(self, name):
        self.name = name

    def set_start_urls(self, start_urls):
        self.start_urls = start_urls