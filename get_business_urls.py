# Import required modules
from lxml import html
import requests
import json

# method to get all business urls
def get_business_urls(page):
    tree = html.fromstring(page.content)
    # Corrected XPath for URL extraction
    urls = tree.xpath('//div[@class="content-nowon-newday"]/h3/a/@href')
    return urls

# method to save business urls on file json
def save_business_urls(urls):
    with open('business_urls.json', 'w') as outfile:
        json.dump(urls, outfile)

# get all business urls of all pages
def get_all_business_urls():
    urls = []
    for i in range(0, 7):
        # Proper string formatting for the URL
        url = f'https://www.marocannuaire.org/Annuaire/activite_ville.php?pageNum_re_aff_dernier_anscri_index={i}&totalRows_re_aff_dernier_anscri_index=80&activite=Restaurants&ville=RABAT%20SALE'
        page = requests.get(url)
        if page.status_code == 200:
            urls += get_business_urls(page)
        else:
            print(f"Failed to fetch URL for page {i}")

    return urls

try:
    urls = get_all_business_urls()
    save_business_urls(urls)
    print('Business URLs saved successfully.')
except Exception as e:
    print(e)
    print('Error while getting or saving business urls')
