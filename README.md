# Scraper
 Version bêta du système de surveillance des prix pour [Books Online](http://books.toscrape.com/).
 
## Description
Un script Python permettant de récupérer les données ci-dessous au moment de l'exécution :

- product_page_url
- universal_ product_code (upc)
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url
- fichiers au format .csv
- images de tous les livres

### Installation

Prérequis :
- Une version de Python v3.10 sera nécéssaire afin de pouvoir utiliser le script.
- Un environnement virtuel venv
- Une version de Git v2.38

Depuis votre terminal ou Git Bash utilisez la commande : \
`python -V` afin de connaitre la version installée sur votre système \
`python -m venv --help` afin de vérifier que vous disposer du module venv \
sinon vous pouvez le télécharger sur https://www.python.org/downloads/ \
`git --version` : pour vérifier la version de git installée sur votre système \
sinon vous pouvez la télécharger sur https://git-scm.com/downloads/ \
***Rappel : les commandes ci-dessus ne sont valables qu'avec le module venv*** \
