# -*- coding: utf-8 -*-
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        details = response.xpath("//*[@class='product_pod']")  
        for detail in details:
            Book_Title = detail.xpath(".//h3/a/@title").extract_first()#Extracting book title 
            Price = detail.xpath(".//*[@class ='price_color']/text()").extract_first()# Extracting price of the book  
            yield {'Book_Title': Book_Title ,'Price' : Price}# Yield the values in dictionary format
        next_url = response.xpath("//*[@class='next']/a/@href").extract_first()# url to navigate to next webpage   
        abs_url = response.urljoin(next_url)# concat main url with refrence url i.e "http://books.toscrape.com/" + "catalogue/page-2.html"
        yield scrapy.Request(abs_url)# Request to parse the next url details. Call parse().


