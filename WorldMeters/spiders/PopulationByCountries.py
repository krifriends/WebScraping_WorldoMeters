# -*- coding: utf-8 -*-
import scrapy
import logging

class PopulationbycountriesSpider(scrapy.Spider):
    name = 'PopulationByCountries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries =response.xpath("//td/a")
        for country in countries:
            countryName = country.xpath(".//text()").get()
            urlName = country.xpath(".//@href").get()

            #Method-1: 
            # abs_url = f"https://www.worldometers.info{urlName}"

            #Method-2:
            #abs_url = response.urljoin(urlName)
            #yield scrapy.Request(url=abs_url)

            #Method-3:
            yield response.follow(url=urlName, callback = self.parseCountry)
    
    def parseCountry(self, response):
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yield{
                'year':year,
                'population':population
            }
