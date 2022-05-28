import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://g1.globo.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div._evt'):
            yield {
                'text': quote.css('span.bstn-hl-title::text').get(),
                # 'link': quote.css('div.bstn-hl::text').get()
            }
        # for quote in response.css('div.feed-post-body-title'):
        #     yield {
        #         'text': quote.css('div._evt a.feed-post-link::text').get(),
        #         'link': quote.css('div._evt a.feed-post-link::attr(href)').get()
        #     }
        # next_page = response.css('div.load-more a::attr(href)').get()
        # if next_page is not None:
        #     yield scrapy.Request(next_page, callback=self.parse)
