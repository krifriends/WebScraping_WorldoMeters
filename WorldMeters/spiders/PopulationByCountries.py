# -*- coding: utf-8 -*-
import scrapy


class PopulationbycountriesSpider(scrapy.Spider):
    name = 'PopulationByCountries'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries =response.xpath("//td/a")
        for country in countries:
            countryName = country.xpath(".//text()").get()
            urlName = country.xpath(".//@href").get()

            yield{
            'countryNames':countryName,
            'urls':urlName
            }

        