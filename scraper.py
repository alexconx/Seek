import requests
from bs4 import BeautifulSoup
import scraperwiki

list_name = []
    
#Loop to get the n first pages
n = 3
for i in range (1,15) :
    page = requests.get("https://www.seek.com.au/jobs-in-construction?page="+str(i))
    soup = BeautifulSoup(page.content, 'html.parser')

    for a in soup.find_all('a', href=True, class_='_257MqcB'):
        print(type(a.getText()))
        list_name.append(a.getText())        
        
print(len(list_name))

for i in range (0, len(list_name)-1) :
    scraperwiki.sqlite.save(unique_keys=['company_name'], data={"company_name": list_name[i]})
