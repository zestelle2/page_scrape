import scrapy

class QuotesSpider(scrapy.Spider):
    i = 1
    name = "citation"
    start_urls = [
        'http://citation-celebre.leparisien.fr/liste-citation',
    ]

    def parse(self, response):

        while self.i< 101:
            #On selectionne la div de la citation citation et sa classe citation
            for citation in response.css('div.citation'):
                yield {
                    'citation': citation.css('div.laCitation a::text').extract_first(),
                    'autheur' : citation.css('div.additionalInformation a::text').extract_first()
                }
            #affichage
            print str(self.i) + " page scrappees."
            
            #page suivante on doit parse i en str
            next_page = response.urljoin("http://citation-celebre.leparisien.fr/liste-citation?page="+str(self.i))
            #incrementation
            self.i = self.i + 1
            #on scrap les donnees
            yield scrapy.Request(next_page, callback=self.parse)

        
            







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