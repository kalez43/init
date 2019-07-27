"""
author: kalez@github.com
description:
"""

import marley as doggie
import requests
from bs4 import BeautifulSoup

response = requests.get("https://theskimm.com/news/daily-skimm")

# print(response.text)

html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

print(soup.title)

print(soup.find_all("link"))

links = soup.find_all("link")

for link in links:
    print(link)

thebest = doggie.sum(1,5)

print(thebest)

doggie.flyer()

print(doggie.num_1)

