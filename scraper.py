
import time
import re
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import scraperwiki

list_url = []

page = requests.get("https://www.gumtree.com.au/s-construction/c18346?ad=offering&ad=offering")
soup = BeautifulSoup(page.content, 'html.parser')

for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])
    
for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])
    
for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--premium user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])

#BOUCLE POUR CHERCHER TOUS LES LIENS DES 15 PREMIERES PAGES
for i in range (2,3) :
    page = requests.get("https://www.gumtree.com.au/s-construction/page-"+str(i)+"/c18346?ad=offering&ad=offering")
    soup = BeautifulSoup(page.content, 'html.parser')

    #There are 3 classes of links
    for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
        list_url.append("https://www.gumtree.com.au"+a['href'])
    for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
        list_url.append("https://www.gumtree.com.au"+a['href'])
    
print (list_url)

scraperwiki.sqlite.save(unique_keys=['id'], data={"id" : "0", "link": list_url[0]})

html = scraperwiki.scrape("https://www.gumtree.com.au/j-vac-phone-get.json?token=1174339848%7C1529906358437%7C6932f7828289d4d34f961a7f5877d387%7Cb4c92b5fdbcf5441db75c70214c13b82%7Cbcf0cc943c497cedbc16e504824ce5fd%7Cdc0eadaa4b7a8c2ab665073df885c2dc")
print html
