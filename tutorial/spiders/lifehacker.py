# -*- coding: utf-8 -*-
import scrapy


class LifehackerSpider(scrapy.Spider):
    name = 'lifehacker'
    allowed_domains = ['https://lifehacker.com/what-i-wish-i-knew-when-i-started-my-career-as-a-softwa-1681002791']
    start_urls = ['https://lifehacker.com/what-i-wish-i-knew-when-i-started-my-career-as-a-softwa-1681002791/']

    def parse(self, response):
        strong = response.css('strong::text').extract()
        text = response.css('p::text').extract()
        for item in zip(strong, text):
            info = {
                'title' : item[0],
                'text' : item[1]
            }
        
            yield info
