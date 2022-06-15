import scrapy
from scrapy_splash import SplashRequest


class Spider(scrapy.Spider):
    name = 'spider'

    def start_request(self):
        # url = 'https://coinmarketcap.com'
        yield SplashRequest(url)

    def parse(self, response):
        # coins = response.xpath('//table//tr')
        for coin in coins:
            yield{
                # 'coin': coin.xpath('//p[@class="sc-1eb5slv-0 hKkaxT"]').get()
            }
