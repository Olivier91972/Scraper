import requests
from bs4 import BeautifulSoup as bs
import csv

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


def get_description_produit():
    main_html = html_parser_livre()
    content_p = main_html.find('article', class_='product_page')
    content_p = content_p.find_all('p')[3].text
    return content_p


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


def get_image_url():
    main_html = html_parser_livre()
    image_img = main_html.find_all('img')[0]
    image_src = image_img.get("src").replace("../../", "")
    image_url_cplt = url_site + image_src
    return image_url_cplt

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


content = get_produit_url()
infos = get_produit_code_prix_stock()
titre = get_titre()
content_p = get_description_produit()
catego = get_categorie()
p = get_nb_etoiles()
image_url_cplt = get_image_url()
infos_livre = {
    'product_page_url': content,
    'universal_product_code(upc)': infos['UPC'],
    'title': titre,
    'price_including_tax': infos['Price (incl. tax)'],
    'price_excluding_tax': infos['Price (excl. tax)'],
    'number_available': infos['Availability'],  # list replace "(" pour laisser uniquement "14"
    'product_description': content_p,
    'category': catego,
    'review_rating': p,  # mettre 1 au lieu de One
    'image_url': image_url_cplt
}



# On prend tout le texte dans un fichier csv
# Créer une liste pour les en-têtes
en_tete = ["product_page_url", "universal_ product_code (upc)", "title", "price_including_tax",
           "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]
# Créer un nouveau fichier pour écrire dans le fichier appelé « phase1.csv »
with open('phase1.csv', 'w') as fichier_csv:
    # Créer un objet writer (écriture) avec ce fichier
    writer = csv.writer(fichier_csv, delimiter=',')
    writer.writerow(en_tete)
    # Parcourir les infos du livre - zip permet d'itérer sur deux listes ou plus à la fois
    for infos_livre in zip(content, infos['UPC'], titre, infos['Price (incl. tax)'], infos['Price (excl. tax)'], 
                           infos['Availability'], content_p, catego, p, image_url_cplt):
        # Créer une nouvelle ligne avec les infos à ce moment de la boucle
                ligne = [content, infos['UPC'], titre, infos['Price (incl. tax)'], infos['Price (excl. tax)'],
                         infos['Availability'], content_p, catego, p, image_url_cplt]
                
    writer.writerow(ligne)



if __name__ == "__main__":
    # html_parser_site()
    #print(get_image_url())
    print(ligne)
#    print("Dans le site Books_to_Scrape, il y a", len(categories), "Categories")


    # def get_infos_livre(url_livre):
    # "Love is a mixtape" et de les exporter dans un fichier phase1.csv
    # qui va se créer automatiquement C:\Users\olivier\PycharmProjects

# url_page_web =
# def get_url_page_web()
