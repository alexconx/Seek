# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

list_url = []

page = requests.get("https://www.gumtree.com.au/s-construction/c18346?ad=offering&ad=offering")
soup = BeautifulSoup(page.content, 'html.parser')

for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])
    
for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])
    
for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--premium user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    list_url.append("https://www.gumtree.com.au"+a['href'])

#for i in range (2,15) :
 #   page = requests.get("https://www.gumtree.com.au/s-construction/page-"+str(i)+"/c18346?ad=offering&ad=offering")
  #  soup = BeautifulSoup(page.content, 'html.parser')

    #3 classes of link
   # for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    #    list_url.append("https://www.gumtree.com.au"+a['href'])
   # for a in soup.find_all('a', href=True, class_='user-ad-row user-ad-row--featured-or-premium user-ad-row--no-image link link--base-color-inherit link--hover-color-none link--no-underline'):
    #    list_url.append("https://www.gumtree.com.au"+a['href'])
    
print (list_url)

page = requests.get(list_url[0])
soup = BeautifulSoup(page.text, 'html.parser')
#elem = webdriver.find_element_by_class_name('c-text-link reply-form__reveal-phone-link').click()
#soup.find_all("script", class_= 'page-container container')

#print soup.prettify().encode('utf-8')




all_scripts = soup.find_all('script')

data = json.loads(all_scripts[-29].get_text())

print('key:', data.keys())
#print('key:', data['TAB'].keys())
