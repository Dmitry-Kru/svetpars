import scrapy


class SvetparsSpider(scrapy.Spider):
    name = "svetpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru"]

    def parse(self, response):
        pass
