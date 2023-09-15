# Import required modules
from lxml import html
import requests
import json


######
# Xpaths ::
####
## Business Data xpaths
name_xpath =''
image_url_xpath = ''
category_xpath = ''
address_xpath = ''
city_xpath = ''
phone_xpath = ''
mobile_xpath = ''
email_xpath = ''
website_xpath = ''
description_xpath = ''




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
