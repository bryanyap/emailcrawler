from emailcrawler.items import EmailcrawlerItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


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