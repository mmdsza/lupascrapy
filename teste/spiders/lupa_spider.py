import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector

class LupaSpider(Spider):
    name = "lupa"
    allowed_domains = ["piaui.folha.uol.com.br"]
    start_urls=["https://piaui.folha.uol.com.br/lupa/"]

    def parse(self, response):
        sel = Selector(response)
        containers = sel.xpath("//div[contains(@class, 'bloco')]")
        for container in containers:
            title = container.xpath("//h2[contains(@class,'bloco-title')]").extract()
            print(title)
