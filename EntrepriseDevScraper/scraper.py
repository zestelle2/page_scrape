import scrapy
import random

class QuotesSpider(scrapy.Spider):
    i = 1
    name = "information"
    start_urls = [
        'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=developpement%20web&ou=Auvergne-Rh%C3%B4ne-Alpes&idOu=R84&page=3&contexte=Cqwfk/o1QAfJ8qdgYXnnKQ%3D%3D&proximite=0&quoiQuiInterprete=developpement%20web',
    ]

    def parse(self, response):
        #On selectionne la section article
        for information in response.css('article.bi-bloc'):
            yield {
                'Nom de lentreprise': information.xpath('//h2/text()').extract()
            }
            print ("MIAMMMMMMMMMMMMM" + response.css('article.bi-bloc'))

        #affichage
        print str(self.i) + " page scrappees."

        #page suivante on doit parse i en str
        next_page = response.urljoin("https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=developpement%20web&ou=Auvergne-Rh%C3%B4ne-Alpes&idOu=R84&page=4&contexte=Cqwfk/o1QAfJ8qdgYXnnKQ%3D%3D&proximite=0&quoiQuiInterprete=developpement%20web")
        #incrementation
        # self.i = self.i + 1
        #on scrap les donnees
        yield scrapy.Request(next_page, callback=self.parse)
            

