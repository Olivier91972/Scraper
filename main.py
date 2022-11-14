import requests
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd
import time


url_site = "http://books.toscrape.com/"
url_livre = "http://books.toscrape.com/catalogue/love-is-a-mix-tape-music-1_711/index.html"
url_categorie = "http://books.toscrape.com/catalogue/category/books/childrens_11/index.html"


# Utilisation de requests/beautifulsoup4 pour parser le Html
def html_parser(url):
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    return soup



def get_produit_url():
    content = url_livre
    return content


# On récupère un dictionnaire des infos code prix et stock
def get_produit_code_prix_stock():
    main_html = html_parser(url_livre)
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
    main_html = html_parser(url_livre)
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
    main_html = html_parser(url_livre)
    titre = main_html.find('title').text
    titre = titre.strip()
    return titre


def get_categorie():
    main_html = html_parser(url_livre)
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


"""
def get_categorie_2():
    main_html = html_parser_site()
    content = main_html.find('ul', class_='nav-list')
    get_links = content.findAll('a')
    categories_names_2 = []
    for link in get_links:
        if 'http' not in link:
            # url_complete = '{}{}'.format(url_site, link['href'])
            categorie_name = link.text.strip()
            categories_names_2.append(categorie_name)
            
    categories_names_2 = categories_names_2[10]
    return categories_names_2
"""


# content_inner > article > div.row > div.col-sm-6.product_main > p.star-rating.One
def get_nb_etoiles(): # Fini, Affiche le nombre d'étoiles
    # Récupère l'url de la page web
    main_html = html_parser(url_livre)
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
    main_html = html_parser(url_livre)
    image_img = main_html.find_all('img')[0]
    image_src = image_img.get("src").replace("../../", "")
    image_url_cplt = url_site + image_src
    return image_url_cplt


#def get_categories_url(): # PAGINATION ET FICHIER CSV A NETTOYER !!!!
    # Pagination
url = "http://books.toscrape.com/catalogue/category/books/childrens_11/index.html"


def get_soup(url):
    """Takes a URL and returns a BeautifulSoup() instance representing the HTML of the page."""
    
    response = requests.get(url)
    html = response.text
    soup = bs(html, "html.parser")

    return soup

def get_soup_test(url):
    response = requests.get(url)
    html = response.text
    soup = bs(html, "html.parser")
    return soup

def get_info_livres_test():
    soup = get_soup(url)
    #print(soup)
    conten = soup.find('article', class_="product_pod")
    conte = conten.article.get('href')
    lie = []
    lien = []
    #print(a['href'])
    for lie in conten:
        lien.append(lie)
        #get_produit_url_test(url)
    return lien
    
    

def get_produit_url_test(url):
    content = url
    return content

# Vu sur Stack Overflow à revoir avec Guillaume !!!
def scrape_page(url):
    """Takes a page and append link of the books that are on the page to global list"""
    BASE_URL = 'http://books.toscrape.com/catalogue/'

    soup = get_soup(url)
    for x in soup.find_all("article", class_="product_pod"):
        url = x.div.a.get('href')
        link = BASE_URL + url
        if x not in book_url:
            book_url.append(link)
    if soup.select_one('li.next a[href]'):
        #print(soup.select_one('li.next a[href]'))
        nextpage = BASE_URL + soup.select_one('li.next a[href]')['href']
        time.sleep(1)
    else:
        nextpage = None

    return nextpage


def scrape_all_pages(url):
    """Scrapes all pages, returning a list of book links."""
    while True:
        if url:
            print(url)
            url = scrape_page(url)
        else:
            break
    return book_url

book_url = []

#scrape_all_pages('https://books.toscrape.com/catalogue/category/books/childrens_11/')


"""
    cat_url_liste = "http://books.toscrape.com/catalogue/category/books/childrens_11/page-"# 2.html

    url_liste = []
    
    for base_url in cat_url_liste:
        verif_page = True
        
        while verif_page is True:   
            i = 1
            url_p = cat_url_liste + str(i) + ".html"
            print(url_p)
            soup_p = html_parser_site()
            derniere_page = soup_p.find("li", class_="next")
            # derniere_page = soup_p.find("center")
            # derniere_p = derniere_page.find_all("li",)
            # print(derniere_page)
            if derniere_page:
                print("Pages chargées !")
                verif_page = False

            else:
                url_liste.append(url_p)
                i = i + 1
                print(url_liste)
                return verif_page
"""


   


"""
    main_html = html_parser_categorie()
    #cat_h3 = main)_html.find_all(a['href'])
    cat_href = main_html.find_all("div", {"class": "image_container"})
    #cat_href = main_html.find("div", {"class": "image_container"})
    #cat_a = cat_href.findAll('a')
    #inner = cat_a.findChildren()
    #cat_href = main_html.findAll('ol', class_='row')
    liens_fin_url = []
    for a in cat_href:
        # On récupère les liens des livres en utilisant find_all de la manière suivante 
        # pour trouver chaque 'a' élément qui a un 'href' attribut, et imprimer chacun
        liens_href = a.findAll('a', href=True)
        for link in liens_href:
            liens_fin_url.append(url_site + "catalogue/" + link['href'].replace("../../../", "") + "\n")
    # print(liens_fin_url)
    liens_fin_url_cplt = liens_fin_url
    return liens_fin_url_cplt


cat_url = get_categorie()
liens_fin_url_cplt = get_categories_url()
categories_names_2 = get_categorie_2()
infos_liens_cat = {
    'Catégorie': categories_names_2,
    'Url page produit': cat_url
    
}


# def save_page_url_cat():
# On prend tout le texte dans un fichier csv
# Créer une liste pour les en-têtes
en_tete_2 = ["Catégorie", "Url page produit"]
# Créer un nouveau fichier pour écrire dans le fichier appelé « phase2.csv »
with open('phase2.csv', 'w') as fichier_csv:  # ", f_csv): au lieu de "as f_csv):" pour mise en attente !!!
    # Créer un objet writer (écriture) avec ce fichier
    writer_2 = csv.writer(fichier_csv, delimiter=',')
    writer_2.writerow(infos_liens_cat)
# Parcourir les infos du livre - zip permet d'itérer sur deux listes ou plus à la fois
    for page_livre in zip(categories_names_2, liens_fin_url_cplt):
    # Créer une nouvelle ligne avec les infos à ce moment de la boucle
        ligne_2 = [categories_names_2, liens_fin_url_cplt]

    writer_2.writerow(ligne_2)
"""

    

# Categories avec Guillaume
def get_categories():
    main_html = html_parser(url_site)
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
    liens.pop(0)
    categories_names.pop(0)
    return liens, categories_names


def get_all_books_links():
    categories_url, categories_names = get_categories()
    for categories_url in categories_url:
        links = get_links_categorie()


def get_links_categorie(categorie_url):
    main_html = html_parser(categorie_url)
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
#tableau = pd.DataFrame(infos_livre)

pd_infos_livre = pd.Series(infos_livre, index=["product_page_url", "universal_ product_code (upc)", "title", "price_including_tax", 
                                               "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"])


"""
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
"""


if __name__ == "__main__":
    cts_urls, cts_names = get_categories()
    for cts_url in cts_urls:
        print(cts_url)