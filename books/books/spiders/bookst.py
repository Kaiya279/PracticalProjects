# -*- coding: utf-8 -*-
import scrapy
from time import sleep
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException

class BookstSpider(Spider):
    name = 'bookst'
    allowed_domains = ['books.toscrape.com/']

    def start_requests(self):
        self.driver=webdriver.Chrome('C:/Users/lenovo/Desktop/quotes_spider/chromedriver')
        self.driver.get('http://books.toscrape.com/')
        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()
        for book in bookst:
            url='http://books.toscrape.com/'+book
            yield Request(url,callback=self.parse_book)

        while True:
            try:
                next_page = driver.find_element_by_xpath('//a[text()="next"]')
                sleep(3)
                self.logger.info('Sleeping for 3 seconds.')
                next_page.click()

                sel=Selector(text=self.driver.page_source)
                books = sel.xpath('//h3/a/@href').extract()
                for book in bookst:
                    url = 'http://books.toscrape.com/catalogue/' + book
                    yield Request(url, callback=self.parse_book)
                    
            except  NoSuchElementException:
                self.logger.info('No more pages to load.')
                self.driver.quit()
                break
                pass
            
    def parse_book(self,response):
        pass
