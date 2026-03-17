import scrapy


class MyfirstspiderSpider(scrapy.Spider):
    name = "myFirstSpider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        articles = response.css( 'article.product_pod' )

        for article in articles:
            yield{
                'name'  : article.css( ' h3 a::text ' ).get(),
                'price' : article.css( ' div.product_price p ').get(),
                'URL'   : article.css( ' h3 a ' ).ttrib['href']
            }
