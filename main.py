import requests
from bs4 import BeautifulSoup as bs

url_site = "http://books.toscrape.com/"
url_livre = "http://books.toscrape.com/catalogue/love-is-a-mix-tape-music-1_711/index.html"
# print(url_site)


# Utilisation de requests/beautifulsoup4 pour parser le Html
def html_parser():
    page = requests.get(url_site)
    soup = bs(page.content, 'html.parser')
    # print(soup)
    return soup


if __name__ == "__main__":
    html_parser()

    # def get_infos_livre(url_livre):
    # "Love is a mixtape" et de les exporter dans un fichier phase1.csv
    # qui va se créer automatiquement C:\Users\olivier\PycharmProjects


# url_page_web =
# def get_url_page_web()

"""
    infos_livre = {
    'product_page_url' :
    'universal_product_code(upc)' :
    'title':
    'price_including_tax' :
    'price_excluding_tax' :
    'number_available' :
    'product_description' :
    'category' :
    'review_rating' :
    'image_url' :
    }
"""


# def get_page_url():
# Récupère l'url de la page web
#    page_url =
#    return

# def get_code_produit():
