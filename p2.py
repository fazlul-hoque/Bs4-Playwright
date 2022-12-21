

#https://stackoverflow.com/questions/74297460/scrapy-playwright-does-not-send-the-next-request-via-scrapy/74300333#74300333#



import scrapy
from scrapy_playwright.page import PageMethod

class TestSpider(scrapy.Spider):
    name = "test"
    def start_requests(self):
        yield scrapy.Request(

            url="https://info.uniswap.org/#/",
            callback=self.parse,
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", '((//*[@class="sc-brqgnP klmLHi"])[1]//*[@class="sc-brqgnP klmLHi"])[1]'),
                ],
            },
        )

    def parse(self, response):
        
        products = response.xpath('((//*[@class="sc-brqgnP klmLHi"])[1]//*[@class="sc-brqgnP klmLHi"])[1]//div[@class="sc-bXGyLb ePvtyo"]')
        for product in products:
            yield {
            'price':product.xpath('.//*[@class="sc-chPdSV goKJOd sc-bMVAic eOIWzG css-63v6lo"][1]/text()').get(),
          
            }