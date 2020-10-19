import csv
import requests
from bs4 import BeautifulSoup
import urllib.parse

url_home = 'http://books.toscrape.com/'
url_produit = 'http://books.toscrape.com/catalogue/in-a-dark-dark-wood_963/index.html'
response = requests.get(url_produit)


if response.ok:
    soupe = BeautifulSoup(response.text, features="html.parser")
    product_page_url = url_produit
    
def SearchInBoard(id, soup):
    for i in soup.find_all("th"):
        if i.text.strip() == id:
            return(i.find_next("td").text.strip())

def SearchDescription(soup):
    description = soup.find_all(['p'])
    return(description[3].text.strip())

def SearchTitle(soup):
    return(soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1').text.strip())

def SearchCategory(soup):
    category = soup.find('ul', {'class': 'breadcrumb'}).find_all(['a'])
    return(category[2].text.strip())

def SearchImageUrl(soup, url):
    img = soup.find('div', {'class': 'thumbnail'}).find('div', {'class': 'carousel-inner'}).find('div', {'class': 'item active'}).find('img')
    link = img['src']
    return urllib.parse.urljoin(url, link)


universal_product_code = SearchInBoard("UPC", soupe)
price_including_tax = SearchInBoard("Price (incl. tax)", soupe)
price_excluding_tax = SearchInBoard("Price (excl. tax)", soupe)
number_available = SearchInBoard("Availability", soupe)
review_rating = SearchInBoard("Number of reviews", soupe)
product_description = SearchDescription(soupe)
title = SearchTitle(soupe)
category = SearchCategory(soupe)

image_url = SearchImageUrl(soupe, url_home)



print(image_url)

"""
    -Ecrire les données dans un fichier CSV en colonne avec
    les valeurs ci dessus comme en-tête
"""

        #Seconde Etape#

"""
    -Etendre le script afin de récupérer toutes les données d'une
    catégorie

    -Attention au passage d'une page à l'autre
"""

        #Troisième Etape#

"""
    -Parcourir toutes les catégories et récupérer les infos
    de tous les produits dans autant de fichiers CSV qu'il
    y a de catégories
"""

        #Quatrième Etape#
"""
    Télécharger et enregistrer le fichier image de chaque livre
"""