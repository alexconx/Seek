
import time
import re
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import scraperwiki

list_url = []
list_location = []

page = requests.get("https://www.gumtree.com.au/s-construction/c18346?ad=offering&ad=offering")
soup = BeautifulSoup(page.content, 'html.parser')

for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])
    
for span in soup.find_all('span', class_='user-ad-row__location-area'):
    print (span['user-ad-row__location-area'])
    
for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])
    
for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--premium user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])

#BOUCLE POUR CHERCHER TOUS LES LIENS DES 15 PREMIERES PAGES
for i in range (2,10) :
    page = requests.get("https://www.gumtree.com.au/s-construction/page-"+str(i)+"/c18346?ad=offering&ad=offering")
    soup = BeautifulSoup(page.content, 'html.parser')

    #There are 3 classes of links
    for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
        list_url.append("https://www.gumtree.com.au"+a['href'])
    for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
        list_url.append("https://www.gumtree.com.au"+a['href'])
    
print (list_url[0])

for i in range (0, len(list_url)-1) :
    scraperwiki.sqlite.save(unique_keys=['id'], data={"id" : str(i), "link": list_url[i]})
