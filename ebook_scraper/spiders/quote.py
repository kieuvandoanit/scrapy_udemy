import scrapy
from scrapy.selector import Selector
from scrapy_playwright.page import PageMethod
import json

# proxy: 45.61.186.166
class QuoteSpider(scrapy.Spider):
    name = "quote"

    def start_requests(self):
        yield scrapy.Request(
            url="https://quotes.toscrape.com/api/quotes?page=1",
            meta = {
                'proxy': '45.61.186.166'
            }
        )

    async def parse(self, response):
        data = json.loads(response.body)
        yield data
