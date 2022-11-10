import requests
from bs4 import BeautifulSoup as bs

url_site = "http://books.toscrape.com/"
url_livre = "http://books.toscrape.com/catalogue/love-is-a-mix-tape-music-1_711/index.html"


# Utilisation de requests/beautifulsoup4 pour parser le Html
def html_parser_site():
    response = requests.get(url_site)
    soup_site = bs(response.content, 'html.parser')
    return soup_site


def html_parser_livre():
    response = requests.get(url_livre)
    soup_livre = bs(response.content, 'html.parser')
    return soup_livre


def get_livres_url():
    main_html = html_parser_site()


def get_produit_url():
    content = url_livre
    return content


# On récupère un dictionnaire des infos code prix et stock
def get_produit_code_prix_stock():
    main_html = html_parser_livre()
    content = main_html.find('table', class_='table table-striped')
    code_upc = content.findAll('tr')
    infos = {}
    for ifs in code_upc:
        infos[ifs.findChildren()[0].text] = ifs.findChildren()[1].text
    return infos


# On créer un objet infos avec la methode pour selectionner la clé
def get_code_produit():
    infos = get_produit_code_prix_stock()
    return infos['UPC']


def get_prix_ht():
    infos = get_produit_code_prix_stock()
    return infos['Price (excl. tax)']


def get_prix_ttc():
    infos = get_produit_code_prix_stock()
    return infos['Price (incl. tax)']


def get_stock():
    infos = get_produit_code_prix_stock()
    return infos['Availability']


def get_page_url():
    main_html = html_parser_site()
    content = main_html.find('a')
    link = '{}{}'.format(url_site, content['href'])
    return link


"""
    books_link = get_all_books_url(data)
         for book_url in  books_link:
            print('data collection : ', book_url)
            try:
               data = get_book_info(book_url)
"""


def get_titre():
    main_html = html_parser_livre()
    titre = main_html.find('title').text
    titre = titre.strip()
    return titre


def get_categorie():
    main_html = html_parser_livre()
    categorie = main_html.find('ul', class_='breadcrumb')
    get_links = categorie.findAll('a')
    catego = []
    categos = []
    for cat in get_links:
        catego = cat.text
        categos.append(catego)
    # Bloqué 1h à cause de l'indentation et list()[]
    catego = list(categos)[2]
    return catego


# content_inner > article > div.row > div.col-sm-6.product_main > p.star-rating.One
def get_nb_etoiles(): # Fini, Affiche le nombre d'étoiles
    # Récupère l'url de la page web
    main_html = html_parser_livre()
    page_url = main_html.find_all('p', {"class": "star-rating One"})
    p = []
    tablep = []
    tablesp = []
    for p in page_url:
        tablep = p
        tablesp.append(tablep)
    return p.get("class")[1]
    
    
    # Bloqué 1h à cause de l'indentation et list()[]
    #nb_etoiles = list(categos)[2]
    #return nb_etoiles


def get_categories():
    main_html = html_parser_site()
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
    get_links = content.findAll('a')# All ou _all???? voir
    # stack car depuis 2016 'findAll' has been renamed to 'find_all'. Link to official documentation


    liens = []
    for link in get_links:
      if 'http' not in link:
         url_complete = '{}{}'.format(url_site, link['href'])
         liens.append(url_complete)
    return liens


"""
    infos_livre = {
    'product_page_url' : 'get_product_url()'
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
    # html_parser_site()
    print(get_nb_etoiles())

#    print(categories)
#    print("Dans le site Books_to_Scrape, il y a", len(categories), "Categories")


    # def get_infos_livre(url_livre):
    # "Love is a mixtape" et de les exporter dans un fichier phase1.csv
    # qui va se créer automatiquement C:\Users\olivier\PycharmProjects

# url_page_web =
# def get_url_page_web()
