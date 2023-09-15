# Import required modules
from lxml import html
import requests
import json

# Base url
base_url = 'https://www.marocannuaire.org/Annuaire/'

######
# Xpaths ::
####
## Business Data xpaths
name_xpath ='//*[@id="content"]/div/div/div/div[1]/h3/text()'
image_url_xpath = '//*[@id="content"]/div/div/div/div[1]/p[1]/img/@src'
category_xpath = '//*[@id="content"]/div/div/div/div[1]/u[1]/a/strong/text()'
address_xpath = '//*[@id="content"]/div/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/font/ul/li[1]/text()[2]'
city_xpath = '//*[@id="content"]/div/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/font/ul/li[1]/text()[4]'
phone_xpath = '//*[@id="content"]/div/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/font/ul/li[2]/a[1]/u/text()'
mobile_xpath = '//*[@id="content"]/div/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/font/ul/li[2]/a[2]/u/text()'
email_xpath = '//*[@id="content"]/div/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/font/ul/a[1]/text()'
website_xpath = '//*[@id="content"]/div/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/font/ul/li[4]/a/text()'
description_xpath = '//*[@id="content"]/div/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div/div/p[1]/font/text()'




# class of business fields and method that rturn json format
class Business:
    def __init__(self, name, image_url, category, address, city, phone, mobile, email, website, description):
        self.name = name
        self.image_url = image_url
        self.category = category
        self.address = address
        self.city = city
        self.phone = phone
        self.mobile = mobile
        self.email = email
        self.website = website
        self.description = description

    def to_json(self):
        return {
            'name': self.name,
            'image_url': self.image_url,
            'category': self.category,
            'address': self.address,
            'city': self.city,
            'phone': self.phone,
            'mobile': self.mobile,
            'email': self.email,
            'website': self.website,
            'description': self.description
        }




# method to get business data
def get_business_data(url):
    page = requests.get(base_url + url)
    tree = html.fromstring(page.content)
    name = tree.xpath(name_xpath)
    image_url = tree.xpath(image_url_xpath)
    category = tree.xpath(category_xpath)
    address = tree.xpath(address_xpath)
    city = tree.xpath(city_xpath)
    phone = tree.xpath(phone_xpath)
    mobile = tree.xpath(mobile_xpath)
    email = tree.xpath(email_xpath)
    website = tree.xpath(website_xpath)
    description = tree.xpath(description_xpath)
    return Business(name, image_url, category, address, city, phone, mobile, email, website, description)


# method to save business data on file json
def save_business_data(business):
    with open('business_data.json', 'a') as outfile:
        json.dump(business.to_json(), outfile, indent=4)
        outfile.write(',')


# method to get all business data
def get_all_business_data():
    with open('business_urls.json') as json_file:
        urls = json.load(json_file)
        for url in urls:
            try:
                business = get_business_data(url)
                save_business_data(business)
            except Exception as e:
                print(e)
                print('Error while getting business data')


try:
    get_all_business_data()
except Exception as e:
    print(e)
    print('Error while getting business data')