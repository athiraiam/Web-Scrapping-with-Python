# -*- coding: utf-8 -*-
import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        details = response.xpath("//*[@class='product_pod']")  
        for detail in details:
            Book_Title = detail.xpath(".//h3/a/@title").extract_first() 
            Price = detail.xpath(".//*[@class ='price_color']/text()").extract_first()  
            yield {'Book_Title': Book_Title ,'Price' : Price}
        next_url = response.xpath("//*[@class='next']/a/@href").extract_first()   
        abs_url = response.urljoin(next_url)
        yield scrapy.Request(abs_url)


