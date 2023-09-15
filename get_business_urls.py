# Import required modules
from lxml import html
import requests
import json

# Xpath of the last page url
last_page_xpath = '//*[@id="content"]/div/div/div/div[1]/div[3]/a[10]/@href'

# method to get the last page number  pageNum_re_aff_dernier_anscri_index
def get_last_page():
    page = requests.get('https://www.marocannuaire.org/Annuaire/activite_ville.php?pageNum_re_aff_dernier_anscri_index=0&totalRows_re_aff_dernier_anscri_index=80&activite=Restaurants&ville=RABAT%20SALE')
    tree = html.fromstring(page.content)
    # Corrected XPath for the last page URL
    last_page_url = tree.xpath(last_page_xpath)[0]
    # Extract the page number from the URL
    last_page = int(last_page_url.split('=')[1].split('&')[0])
    return last_page

last_page=get_last_page()

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
    # keep tray antil we get the last page
    for i in range(0, last_page + 1):
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
