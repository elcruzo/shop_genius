import scrapy

class ShopGenius(scrapy.Spider):
    name = 'shop_genius_spider'
    
    start_urls = [
        'https://www.amazon.com/',
        'https://www.temu.com/',
        'https://us.shein.com/',
    ]

    def parse(self, response):
        
        product_titles = response.css('span.a-text-normal::text').extract()
        product_titles = response.css('h2.product-title::text').extract()
        product_prices = response.css('span.product-price::text').extract()
        product_prices = response.css('span.a-price span.a-offscreen::text').extract()

        for title, price in zip(product_titles, product_prices):
            yield {
                'title': title.strip(),
                'price': price.strip(),
                'source': response.url,
            }
