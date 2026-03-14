
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
# scrapy genspider myspider books.toscrape.com

#? download scrapy shell
# pip install ipython
# in scrapy.vfg  => shell   = ipython
# scrapy shell

#? Commands
#*  fetch('https://books.toscrape.com/')
#*  response.css( 'article ' )
#*  response.css( 'article.product_pod' )
#*  retriveArticles = response.css( 'article.product_pod' )
#*  retriveArticles.get()    => retrive only the first item