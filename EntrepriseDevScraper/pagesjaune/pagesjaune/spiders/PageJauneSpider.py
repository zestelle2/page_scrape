import re
import scrapy
import random
from scrapy.shell import inspect_response

class PagesJauneSpider(scrapy.Spider):
    i = 0
    name = "numero"
    start_urls = [
        'https://www.pagesjaunes.fr/recherche/region/auvergne-rhone-alpes/developpement-web',
    ]

    def parse(self, response):

        #while self.i< 101:
            #On selectionne la div de la citation citation et sa classe citation

        for lien in response.css('article'):
            numero = ''.join(lien.xpath('//div/@data-pjhistofantomas').extract()).strip() 
            
            print(numero)
            
            numeroReSearch = re.search('data":"([0-9]{10})', numero)
            if(numeroReSearch.group(0)) :
                numero = numeroReSearch.group(0) 
            
            yield {
                'nom de lentreprise': ''.join(lien.css('div.zone-bi span.not-visible::text').extract()).strip(),
                'numero de tel' : numero
            }
            self.i = self.i + 1
        
            







"""class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'texte': quote.css('span.text::text').extract_first(),
                'aautheur': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse) """