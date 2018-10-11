# page_scrape
Le web est basé avec le scraping, on récolte chaque jours des milliers d'informations, on les tries et on les exploites. Ainsi on utilise facilement des données dèja existante. J'ai voulu essayer ce mode en **Python3** à l'aide de la **libraire scrapy** :https://scrapy.org/
```
pip install scrapy
```
J'ai fait 3 minis Projets, dont un qui est en cours, mais ils sont tous améliorables. Chacun récupère des données et on les envoies sur un fichier j.son .le fichier python se nomme scraper.py et contient le code principal. 
```
scrapy runspider scraper.py -o test.json

```
##Projet Citation : 
Avec ce projet, on visualise facilement le pouvoir que détient le scraping. On récupere l'auteur, et la citation sur les 100 premières pages du site en question . On voit facilement, peuvent être facilement scrapés.

##Projet EntrepriseDevScraper :
Dans ce projet, on utilise le site populaire des pages Jaunes. On récupère un numéro de téléphone et le nom de l'entreprise
on à dû lancer un projet nommé : Page Jaune. 
```
 scrapy startproject pagesjaune
```
Si on veux faire facilement du debug, et avoir le Shell de scrapy, on met dans notre fichier .py cette ligne dans la méthode parse :  
```
inspect_response(response, self)
```
On coutourne aussi l'eeur 703 en changeant l'user agent

##Projet videoScraper : 
Récupérer les vidéo Youtube à l'aide avec regex. En cours. https://regex101.com/
