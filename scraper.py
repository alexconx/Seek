
import time
import re
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import scraperwiki

list_url = []
list_date = []
list_location = []

page = requests.get("https://www.gumtree.com.au/s-construction/advertisedby-private/c18346?ad=offering")
soup = BeautifulSoup(page.content, 'html.parser')

for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])
    
for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])
    
for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--premium user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])
    
#Loop to get the n first pages
n = 3
for i in range (2,n) :
    page = requests.get("https://www.gumtree.com.au/s-construction/page-"+str(i)+"/advertisedby-private/c18346?ad=offering")
    soup = BeautifulSoup(page.content, 'html.parser')

    #There are 3 classes of links
    for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
        list_url.append("https://www.gumtree.com.au"+a['href'])
    for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
        list_url.append("https://www.gumtree.com.au"+a['href'])
        
        
print(len(list_url))

for i in range (0, len(list_url)-1) :
    page = requests.get(list_url[i])
    soup = BeautifulSoup(page.content, 'html.parser')
    print(i)
    dl_data = soup.find_all("dd")
    if len(dl_data) > 1 :
        list_date.append(dl_data[1].text)
     else :
         list_date.append("None")            
    loc_data = soup.find(class_='ad-heading__ad-map-link google-map-link j-google-map-link')
    list_location.append(loc_data.text.replace(",", ";"))
    
    scraperwiki.sqlite.save(unique_keys=['link'], data={"link": list_url[i], "date": list_date[i], "location": list_location[i]})
    
print(type(list_url[0]))
print(type(list_date[0]))
print(type(list_location[0]))
