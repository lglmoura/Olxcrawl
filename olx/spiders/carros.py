# -*- coding: utf-8 -*-
import scrapy


class CarrosSpider(scrapy.Spider):
    name = 'carros'
    
    start_urls = ['https://rj.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios/']

    def parse(self, response):
        items = response.xpath(
                '//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]'
            )
        for item in items:
            url = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)
        
        
            
        
    
    def parse_detail(self, response):
        title = response.xpath('//title/text()').extract_first()

        preco = response.xpath(
            '//span[contains(@class,"actual-price")]/text()'
        ).extract_first()
        
        year = response.xpath(
            '//span[contains(text(), "Ano")]/following-sibling::strong/a/@title'
        ).extract_first()
        
        ports = response.xpath(
            '//span[contains(text(), "Portas")]/following-sibling::strong/text()'
        ).extract_first()
        
        combustivel = response.xpath(
            '//span[contains(text(), "Combustível")]/following-sibling::strong/a/@title'
        ).extract_first()

        km = response.xpath(
            '//span[contains(text(), "Quilometragem")]/following-sibling::strong/text()'
        ).extract_first().rstrip().lstrip()

        

        yield {
            'title': title,
            'preco' : preco,
            'year': year,
            'ports': ports,
            'combustivel' : combustivel,
            'km' : km, 
        }
