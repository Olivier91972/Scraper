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
***Rappel : les commandes ci-dessus ne sont valables qu'avec le module venv*** 

Dupplication du dépôt distant en local depuis le terminal ou l'invite de commande : \
`git clone https://github.com/Olivier91972/Scraper.git` 

Création de l'environnement virtuel "venv" : \
utilisez la commande `python -m venv <nom environnement>` dans ce cas, \
"env" sera par convention, le nom environnement, soit `python -m venv env` 

Activation de l'environnement virtuel "env" : \
exécutez `env/Scripts/activate.bat` \
(si vous êtes sous Unix, la commande sera source `env/bin/activate`)

Installation des packages avec pip : \
`pip install -r requirements.txt`

Lancez le script : \
`python main.py` sous Unix \
`py main.py` sous Windows \
Si votre interpreteur est invalide pour le projet : 
`rm -rf env` pour supprimer les données de l'environnement virtuel \
Créez et activez depuis l'interface graphique de votre IDE python

***Rappel : Le script ne doit retourner aucune erreur à la fin de son éxécution. \
La bonne éxécution du script, ainsi que l'intégrité des données récupérées, \
dépendront de la stabilité de votre connexion internet.*** 