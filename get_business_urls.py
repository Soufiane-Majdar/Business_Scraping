
# Import required modules
from lxml import html
import requests
import json

# Request the page
# number of the page 
i=0
page = requests.get('https://www.marocannuaire.org/Annuaire/activite_ville.php?pageNum_re_aff_dernier_anscri_index={i}&totalRows_re_aff_dernier_anscri_index=80&activite=Restaurants&ville=RABAT%20SALE')

print(page.status_code)

######
# Xpaths ::
####
##  Urls of the business
url_xpath = '//div[@class="content-nowon-newday"]/h3/a/@href'





# method to get all business urls
def get_business_urls(page):
    tree = html.fromstring(page.content)
    urls = tree.xpath(url_xpath)
    return urls

# method to save business urls on file json
def save_business_urls(urls):
    with open('business_urls.json', 'w') as outfile:
        json.dump(urls, outfile)


# get all business urls of all pages
def get_all_business_urls():
    urls = []
    for i in range(0, 7):
        page = requests.get('https://www.marocannuaire.org/Annuaire/activite_ville.php?pageNum_re_aff_dernier_anscri_index={i}&totalRows_re_aff_dernier_anscri_index=80&activite=Restaurants&ville=RABAT%20SALE')
        urls += get_business_urls(page)
    return urls

try:
    urls = get_all_business_urls()
    save_business_urls(urls)
except Exception as e:
    print(e)
    print('Error while getting business urls')
