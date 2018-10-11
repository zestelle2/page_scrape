import scrapy

class QuotesSpider(scrapy.Spider):
    i = 1
    objectScraper = 'video'
    # l'expression régular
    video = 'gridVideoRenderer":(.+?),"publishedTimeText'
    start_urls = [
        'https://www.youtube.com/?gl=FR&hl=fr',
    ]

    #le fichier avec le javsacript. 

    # à mettre dans la boucle for patern expression
    m = re.search(video, objectScraper)
    m.group(0)
    'egg'

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
        
