import scrapy
from ebook_scraper.items import EbookItem
from scrapy.loader import ItemLoader

class EbookSpider(scrapy.Spider):
		name = "ebook"
		start_urls = [ "http://www.scrapethissite.com/pages/advanced/?gotcha=csrf" ]
		cols = ["Title", "Price"]

		# def start_requests(self):


		def parse(self, response):
			csrf_token = response.css("input[name='csrf']").attrib["value"]
			print("HIHI")

			print("[ CSRF ]:", csrf_token)
			yield scrapy.FormRequest(
				"http://www.scrapethissite.com/pages/advanced/?gotcha=csrf",
				formdata={
					"user": "john",
					"pass": "__strong__",
					"csrf": csrf_token
				},
				callback=self.parse_login
			)

		def parse_login(self, response):
			print("[ RESULT ]:", response.css("div.row div::text").get().strip())

		# def parse(self, response):
		# 	ebooks = response.css("article.product_pod")
		#
		# 	for ebook in ebooks:
		# 		url = ebook.css("h3 a").attrib["href"]
		#
		# 		yield scrapy.Request(
		# 			url = self.start_urls[0] + url,
		# 			callback = self.parse_details
		# 		)

		# def parse_details(self, response):
		# 	main = response.css("div.product_main")
		#
		# 	loader = ItemLoader(
		# 		item=EbookItem(),
		# 		selector=main
		# 	)
		#
		# 	loader.add_css("title", "h1::text")
		# 	loader.add_css("price", "p.price_color::text")
		#
		# 	quantity_p = main.css("p.availability")
		# 	loader.add_value("quantity", quantity_p.re(r'\(.+ available\)')[0])
		#
		# 	yield loader.load_item()


