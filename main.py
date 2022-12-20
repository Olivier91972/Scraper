import requests
from bs4 import BeautifulSoup as bs
import csv
import time
import os
import urllib.request

global e

url_site = "http://books.toscrape.com/"
url_livre = "http://books.toscrape.com/catalogue/love-is-a-mix-tape-music-1_711/index.html"
url_categorie = "http://books.toscrape.com/catalogue/category/books/childrens_11/index.html"


def html_parser(url):
    # Permet d'obtenir la soupe de bs
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    return soup


def scraper_livre_phase1(url):
    # Création des dossiers et sous dossiers pour les exports
    dossiers = ['data', "data/csv", "data/images"]
    for dossier in dossiers:
        if not os.path.exists(dossier):
            os.mkdir(dossier)
    nom = "livre_ph1"
    filename = 'data/csv/%s.csv' % nom
    # Export csv
    with open(filename, 'w', encoding='utf8', newline='') as fopen:
        writer = csv.writer(fopen, delimiter=',')

        en_tete = ["product_page_url", "universal_product_code", "title", "price_including_tax",
                   "price_excluding_tax", "number_available", "product_description", "category", "review_rating",
                   "image_url"]
        writer.writerow(en_tete)

        source_url = url_site
        soup = html_parser(url)
        li = soup.find("article", class_="product_pod")
        titre = soup.find("div", class_="col-sm-6 product_main")
        titre_s = titre.find("h1").text.encode("ascii", "ignore").decode("ascii")
        print(f'Livre : {titre_s:.^60}')
        info_url = url
        print(f'product_page_url : {info_url}')
        infos = get_produit_code_prix_stock(url)
        code_upc = infos[0]
        print(f'universal_ product_code (upc) : {code_upc}')
        print(f'title : {titre_s}')
        prix_ttc = infos[1]
        print(f'price_including_tax : {prix_ttc}')
        prix_ht = infos[2]
        print(f'price_excluding_tax : {prix_ht}')
        stock = infos[3]
        print(f'number_available : {stock}')
        descr_prod = get_description_produit(url)
        print(f'product_description : {descr_prod}')
        categorie = get_categorie(url)
        print(f'category : {categorie}')
        nb_etoiles = li.find("p", class_="star-rating")["class"][1]
        print(f'review_rating : {nb_etoiles}')
        couv_url_b = soup.find("div", class_="item active")
        couv_url = source_url + couv_url_b.img["src"].replace("../../", "")
        print(f'image_url : {couv_url}')
        time.sleep(1)
        text = "Terminé !"
        print(f' {text:.>60} \n')

        livre = {"product_page_url": info_url,
                 "universal_product_code": code_upc,
                 "title": titre_s,
                 "price_including_tax": prix_ttc,
                 "price_excluding_tax": prix_ht,
                 "number_available": stock,
                 "product_description": descr_prod,
                 "category": categorie,
                 "review_rating": nb_etoiles,
                 "image_url": couv_url}

        info = [info_url, code_upc, titre_s, prix_ttc, prix_ht,
                stock, descr_prod, categorie, nb_etoiles, couv_url]
        writer.writerow(info)
    return livre


def naviguer_et_scraper_phase2():
    page_number = 1
    continue_categorie_scraping, liens_cat = get_links_categorie(url_categorie, page_number=page_number)
    start_time = time.perf_counter()

    dossiers = ['data', "data/csv", "data/images"]
    for dossier in dossiers:
        if not os.path.exists(dossier):
            os.mkdir(dossier)
    nom = "livres_ph2"
    filename = 'data/csv/%s.csv' % nom
    with open(filename, 'w', encoding='utf8', newline='') as fopen:
        writer = csv.writer(fopen, delimiter=',')
        en_tete = ["product_page_url", "universal_product_code", "title", "price_including_tax",
                   "price_excluding_tax", "number_available", "product_description", "category", "review_rating",
                   "image_url"]
        writer.writerow(en_tete)

        for lien in liens_cat:
            source_url = url_site
            html_text = requests.get(lien).text
            soup = bs(html_text, "html.parser")
            titre = soup.find("div", class_="col-sm-6 product_main")
            titre_s = titre.find("h1").text.encode("ascii", "ignore").decode("ascii")
            print(titre_s)
            print(f'Livre : {titre_s:.^60}')
            info_url = lien
            print(f'product_page_url : {info_url}')
            infos = get_produit_code_prix_stock(lien)
            code_upc = infos[0]
            print(f'universal_ product_code (upc) : {code_upc}')
            print(f'title : {titre_s}')
            prix_ttc = infos[1]
            print(f'price_including_tax : {prix_ttc}')
            prix_ht = infos[2]
            print(f'price_excluding_tax : {prix_ht}')
            stock = infos[3]
            print(f'number_available : {stock}')
            descr_prod = get_description_produit(lien)
            print(f'product_description : {descr_prod}')
            categorie = get_categorie(lien)
            print(f'category : {categorie}')
            nb_etoiles = soup.find("p", class_="star-rating")["class"][1]
            print(f'review_rating : {nb_etoiles}')
            couv_url_b = soup.find("div", class_="item active")
            couv_url = source_url + couv_url_b.img["src"].replace("../../", "")
            print(f'image_url : {couv_url}')
            time.sleep(1)
            text = "Livre suivant !"
            print(f' {text:.>60} \n')

            livres = {"product_page_url": info_url,
                      "universal_product_code": code_upc,
                      "title": titre_s,
                      "price_including_tax": prix_ttc,
                      "price_excluding_tax": prix_ht,
                      "number_available": stock,
                      "product_description": descr_prod,
                      "category": categorie,
                      "review_rating": nb_etoiles,
                      "image_url": couv_url}
            info = [info_url, code_upc, titre_s, prix_ttc, prix_ht,
                    stock, descr_prod, categorie, nb_etoiles, couv_url]
            writer.writerow(info)

    elapsed_time = time.perf_counter() - start_time
    elapsed_time_min = int(elapsed_time / 60)
    print(f"The whole process took {elapsed_time_min} minutes "
          f"and {round(elapsed_time - (60 * elapsed_time_min), 2)} seconds.")
    return livres


def naviguer_et_scraper_phase3():
    lien = []
    page_number = 1
    start_time = time.perf_counter()

    with open("infos_livres.csv", 'w', encoding='utf8', newline='') as fopen:  # Ouvre le fichier csv
        writer = csv.writer(fopen, delimiter=',')
        en_tete = ["product_page_url", "universal_product_code", "title", "price_including_tax",
                   "price_excluding_tax", "number_available", "product_description", "category", "review_rating",
                   "image_url"]
        writer.writerow(en_tete)
        get_links_categories(url_site, page_number=1)
        for lien in liens_all:
            source_url = url_site
            html_text = requests.get(lien).text
            soup = bs(html_text, "html.parser")
            titre = soup.find("div", class_="col-sm-6 product_main")
            titre_s = titre.find("h1").text.encode("ascii", "ignore").decode("ascii")
            #print(titre_s)
            print(f'Livre : {titre_s:.^60}')
            info_url = lien
            #print(f'product_page_url : {info_url}')
            infos = get_produit_code_prix_stock(lien)
            code_upc = infos[0]
            #print(f'universal_ product_code (upc) : {code_upc}')
            #print(f'title : {titre_s}')
            prix_ttc = infos[1]
            #print(f'price_including_tax : {prix_ttc}')
            prix_ht = infos[2]
            #print(f'price_excluding_tax : {prix_ht}')
            stock = infos[3]
            #print(f'number_available : {stock}')
            descr_prod = get_description_produit(lien)
            #print(f'product_description : {descr_prod}')
            categorie = get_categorie(lien)
            #print(f'category : {categorie}')
            nb_etoiles = soup.find("p", class_="star-rating")["class"][1]
            #print(f'review_rating : {nb_etoiles}')
            couv_url_b = soup.find("div", class_="item active")
            couv_url = source_url + couv_url_b.img["src"].replace("../../", "")
            #print(f'image_url : {couv_url}')
            time.sleep(1)
            text = "Livre suivant !"
            print(f' {text:.>60} \n')
            livres = {"product_page_url": info_url,
                      "universal_product_code": code_upc,
                      "title": titre_s,
                      "price_including_tax": prix_ttc,
                      "price_excluding_tax": prix_ht,
                      "number_available": stock,
                      "product_description": descr_prod,
                      "category": categorie,
                      "review_rating": nb_etoiles,
                      "image_url": couv_url}
            info = [info_url, code_upc, titre_s, prix_ttc, prix_ht,
                    stock, descr_prod, categorie, nb_etoiles, couv_url]
            writer.writerow(info)

    categories_names = get_categories_names(url_site)
    get_data_to_csv(categories_names)

    elapsed_time = time.perf_counter() - start_time
    elapsed_time_min = int(elapsed_time / 60)
    print(f"The whole process took {elapsed_time_min} minutes "
          f"and {round(elapsed_time - (60 * elapsed_time_min), 2)} seconds.")


liens_cat = []
liens_all = []


def get_links_categorie(categorie_url, page_number):
    url_reduite = categorie_url[:-10] + "page-{}.html"
    form_url = url_reduite.format(str(page_number))
    r = requests.get(form_url)

    if r.status_code == 200:
        html_text = requests.get(form_url).text
        soup = bs(html_text, "html.parser")
        content = soup.find('ol', class_='row')
        liens = []
        #print(f"check bouton next - {form_url}")
        get_links = content.findAll('a')
        url_complete = {}

        for link in get_links:
            if 'http' not in link:
                url_complete = '{}{}'.format(url_site + "catalogue/", link['href'].replace("../../../", ""))
            liens.append(url_complete)
        # gestion des doublons dans la liste
        liens_cat = list(set(liens))
        #print(liens_cat)
        # Ajout des liens obtenus dans un conteneur global
        liens_all.extend(liens_cat)
        #print(liens_all)
        #print(len(liens_all))

        nb_liens_page = len(liens_cat)
        #print(nb_liens_page)
        time.sleep(1)

        if nb_liens_page >= 20:  # ou détection du bouton next
            #print("on doit aller à la page suivante !")
            page_number += 1
            get_links_categorie(categorie_url, page_number)

        else:
            return False

    else:
        return False

    return True, liens_all


def get_links_categories(categorie_url, page_number):
    liens_c = get_categories(categorie_url)
    for url_reduite in liens_c:
        categorie_url = url_reduite
        url_reduite = categorie_url[:-10] + "page-{}.html"
        form_url = url_reduite.format(str(page_number))
        r = requests.get(form_url)
        #print(r)

        if r.status_code == 200:
            html_text = requests.get(form_url).text
            soup = bs(html_text, "html.parser")
            content = soup.find('ol', class_='row')
            liens = []
            print(f"Lien en cours... - {form_url}")
            get_links = content.findAll('a')
            url_complete = {}

            for link in get_links:
                if 'http' not in link:
                    url_complete = '{}{}'.format(url_site + "catalogue/", link['href'].replace("../../../", ""))
                liens.append(url_complete)

            liens_cat = list(set(liens))
            liens_all.extend(liens_cat)
            nb_liens_page = len(liens_cat)
            #print(nb_liens_page)
            time.sleep(1)

            if nb_liens_page >= 20:
                #print("page suivante car nb liens max !")
                page_number += 1

                get_links_categorie(categorie_url, page_number)
            else:
                page_number = 1
                pass

        elif r.status_code == 404:
            #print("Récupération des liens de la page index")
            form_url = form_url[:-11]
            html_text = requests.get(form_url).text
            soup = bs(html_text, "html.parser")
            content = soup.find('ol', class_='row')
            liens = []
            print(f"Lien en cours... - {form_url}")
            get_links = content.findAll('a')
            url_complete = {}
            for link in get_links:
                if 'http' not in link:
                    url_complete = '{}{}'.format(url_site + "catalogue/", link['href'].replace("../../../", ""))
                liens.append(url_complete)

            liens_cat = list(set(liens))
            liens_all.extend(liens_cat)
            print(len(liens_all))
            #print("Lien suivant")
        else:
            return False
        page_number = 1
        #print("on continue !")
        time.sleep(1)
    return liens_all


def get_produit_code_prix_stock(url):
    main_html = html_parser(url)
    content = main_html.find('table', class_='table table-striped')
    code_upc = content.findAll('tr')
    infos = {}
    for ifs in code_upc:
        infos[ifs.findChildren()[0].text] = ifs.findChildren()[1].text
    return infos['UPC'], infos['Price (excl. tax)'], infos['Price (incl. tax)'], infos['Availability']


def get_description_produit(url):
    main_html = html_parser(url)
    content_p = main_html.find('article', class_='product_page')
    content_p = content_p.find_all('p')[3].text
    return content_p


def get_categorie(url):
    main_html = html_parser(url)
    categorie = main_html.find('ul', class_='breadcrumb')
    get_links = categorie.findAll('a')
    catego = []
    categos = []
    for cat in get_links:
        catego = cat.text
        categos.append(catego)

    catego = list(categos)[2]
    return catego


def get_categories(categorie_url):
    main_html = html_parser(categorie_url)
    content = main_html.find('ul', class_='nav-list')
    get_links = content.findAll('a')
    liens_c = []
    for link in get_links:
        if 'http' not in link:
            url_complete = '{}{}'.format(url_site, link['href'])
            liens_c.append(url_complete)
    liens_c.pop(0)
    return liens_c


def get_categories_names(categorie_url):
    main_html = html_parser(categorie_url)
    content = main_html.find('ul', class_='nav-list')
    get_links = content.findAll('a')
    categories_names = []
    for link in get_links:
        if 'http' not in link:
            categorie_name = link.text.strip()
            categories_names.append(categorie_name)
    categories_names.pop(0)
    return categories_names


def get_images_url(images):
    start_time = time.perf_counter()

    dossiers = ['data', "data/csv", "data/images"]
    for dossier in dossiers:
        if not os.path.exists(dossier):
            os.mkdir(dossier)

    for image in images:
        soup = html_parser(image)
        image = soup.find('img', {})
        img_url = image.get('src').replace('../../', '')
        url_complete = url_site + img_url
        img_name = str(img_url.split('/')[-1])
        print(img_name)
        # Téléchargement des images - import urllib.request & import os
        print("downloading {}".format(img_url))
        urllib.request.urlretrieve(url_complete,
                                   os.path.join("\\Users\olivier\PycharmProjects\projects\Scraper\data\images",
                                                img_name))

    elapsed_time = time.perf_counter() - start_time
    elapsed_time_min = int(elapsed_time / 60)
    print(f"The whole process took {elapsed_time_min} minutes "
          f"and {round(elapsed_time - (60 * elapsed_time_min), 2)} seconds.")


def get_data_to_csv(categories_names):
    start_time = time.perf_counter()
    for cat_name in categories_names:
        dico = {}
        filename_r = "infos_livres.csv"
        filename_w = fr'data/csv/livres/%s.csv' % cat_name
        en_tete = ["product_page_url", "universal_product_code", "title", "price_including_tax",
                   "price_excluding_tax", "number_available", "product_description", "category", "review_rating",
                   "image_url"]
        with open(filename_r, 'r', encoding='utf8', newline='') as fichier_input:
            reader = csv.reader(fichier_input, delimiter=',')
            with open(filename_w, 'w', encoding='utf8', newline='') as fichier_output:
                writer = csv.writer(fichier_output, delimiter='|')
                writer.writerow(en_tete)
                for ligne in reader:
                    ligne_livre = ligne
                    print(ligne_livre)
                    if cat_name in ligne_livre:
                        dico[ligne_livre[7]] = ligne_livre
                        fichier_output.write(f'{ligne_livre[0]}|{ligne_livre[1]}|{ligne_livre[2]}|{ligne_livre[3]}|'
                                             f'{ligne_livre[4]}|{ligne_livre[5]}|{ligne_livre[6]}|{ligne_livre[7]}|'
                                             f'{ligne_livre[8]}|{ligne_livre[9]}\n')

    elapsed_time = time.perf_counter() - start_time
    elapsed_time_min = int(elapsed_time / 60)
    print(f"The whole process took {elapsed_time_min} minutes "
          f"and {round(elapsed_time - (60 * elapsed_time_min), 2)} seconds.")


if __name__ == "__main__":

    # scraper_livre_phase1(url_livre)

    # naviguer_et_scraper_phase2()

    naviguer_et_scraper_phase3()

    # liens_all = get_links_categories(url_site, page_number=1)
    # get_images_url(liens_all)

    #categories_names = get_categories_names(url_site)
    #get_data_to_csv(categories_names)
