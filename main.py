import requests
from bs4 import BeautifulSoup as bs

url_site = "http://books.toscrape.com/"
url_livre = "http://books.toscrape.com/catalogue/love-is-a-mix-tape-music-1_711/index.html"


# Utilisation de requests/beautifulsoup4 pour parser le Html
def html_parser():
    response = requests.get(url_site)
    soup_html = bs(response.content, 'html.parser')
    return soup_html


def get_categories():
    main_html = html_parser()
    content = main_html.find('ul', class_='nav-list')
    get_links = content.findAll('a')
    liens = []
    categories_names = []
    for link in get_links:
      if 'http' not in link:
         url_complete = '{}{}'.format(url_site, link['href'])
         categorie_name = link.text.strip()
         liens.append(url_complete)
         categories_names.append(categorie_name)
    return liens, categories_names

def get_all_books_links():
    categories_url, categories_names = get_categories()
    for categories_url in categories_url:
        links = get_links_categorie()

def get_links_categorie(categorie_url):
    main_html = html_parser()
    content = main_html.find('ul', class_='nav-list')
    get_links = content.findAll('a')
    liens = []
    for link in get_links:
      if 'http' not in link:
         url_complete = '{}{}'.format(url_site, link['href'])
         liens.append(url_complete)
    return liens


"""
    infos_livre = {
    'product_page_url' : 'page_url'
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





def get_page_url():
    # Récupère l'url de la page web
    page_url = bs.find_all("p", class_="star-rating One")[3]
    a = td.find(a)
    link = a['href']
    return page_url


def get_categorie():
    categories = []
    categories_bs = bs.find('ul', class_="breadcrumb")


    for categorie in categories_bs:
        categories_bs.append(categorie.string)
    return categories
# On affiche tous les categories de livres
"""
if __name__ == "__main__":
    # html_parser()
    print(get_categories())

#    print(categories)
#    print("Dans le site Books_to_Scrape, il y a", len(categories), "Categories")


    # def get_infos_livre(url_livre):
    # "Love is a mixtape" et de les exporter dans un fichier phase1.csv
    # qui va se créer automatiquement C:\Users\olivier\PycharmProjects

# url_page_web =
# def get_url_page_web()
