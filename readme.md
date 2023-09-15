# Web Scraping Project - 'https://www.marocannuaire.org/'

## Description
This project is a web scraping project that aims to extract data from the website 'https://www.marocannuaire.org/' and save it in a json file.

## Installation
To install the project, you need to clone the repository and install the requirements:
```bash
git clone https://github.com/Soufiane-Majdar/Business_Scraping.git

cd Business_Scraping

pip install -r requirements.txt
```

## Usage
To use the project, you need to run the get_business_urls.py file first to get the urls of all the businesses in the website, then run the get_business_data.py file to get the data of each business and save it in a json file.

### get_business_urls.py url explanation
The get_business_urls.py need a url to start scraping from, the url must be in this format like the following example:
"https://www.marocannuaire.org/Annuaire/activite_ville.php?pageNum_re_aff_dernier_anscri_index=0&totalRows_re_aff_dernier_anscri_index=80&activite=Restaurants&ville=RABAT%20SALE"

in this url, we have to change the following parameter to get the urls of all pages of the website:
index=0 -> index=1 -> index=2 -> ... -> index=namber of pages

so we need to make the url in line 23 look like this:
"https://www.marocannuaire.org/Annuaire/activite_ville.php?pageNum_re_aff_dernier_anscri_index={i}&totalRows_re_aff_dernier_anscri_index=80&activite=Restaurants&ville=RABAT%20SALE"

then just run the get_business_urls.py file
```bash
    python get_business_urls.py
```

### run the get_business_data.py file

you can run the get_business_urls.py file withou any changes
    
```bash
    python get_business_data.py
```

### finaly run the clean_json.py file
this file will clean the json file and remove characters that are not text like \u00e9 , \u00e0 ...
```bash
    python clean_json.py
```

