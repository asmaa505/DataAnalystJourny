
#? what is scrapy?
# Scrapy is a fast high-level web crawling and web scraping framework,
# used to crawl websites and extract structured data from their pages.
# It can be used for a wide range of purposes, from data mining to monitoring and automated testing.

#? in terminal
# pip install scrapy
# pip install --upgrade pip
# scrapy version                 Scrapy 2.14.2
# scrapy startproject + ( project name )
# cd ( project name ) / spiders
# 

#? download scrapy shell
# pip install ipython
# in scrapy.vfg  => shell   = ipython
# scrapy shell

#? Commands
#* scrapy genspider ( spider name ) ( website url )
#*  fetch('https://books.toscrape.com/')
#*  response.css( 'article ' )
#*  response.css( 'article.product_pod' )
#*  retriveArticles = response.css( 'article.product_pod' )
#*  retriveArticles.get()    => retrive only the first item
#*  len( retriveArticles )
#*  article1 = retriveArticles[0]
#*  article1.css( ' h3 a::text ' ).get()       => retrive text
#*  article1.css( ' h3 a' ).attrib['href']     => retrive URL
#*  article1.css( ' div.product_price p::text ' ).get()
#todo  modify on the spider file content
def parse(self, response):
    articles = response.css( 'article.product_pod' )

    for article in articles:
        yield{
            'name'  : article.css( ' h3 a::text ' ).get(),
            'price' : article.css( ' div.product_price p ').get(),
            'URL'   : article.css( ' h3 a ' ).attrib['href']
        }
#*  exit
#*  cd ../
#*  scrapy crawl myFirstSpider
#*  scrapy shell  => to open the shell
#*  response.css( 'li.next a::attr(href)').get()