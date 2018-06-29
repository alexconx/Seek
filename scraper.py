import requests
from bs4 import BeautifulSoup

list_name = []
    
#Loop to get the n first pages
n = 3
for i in range (1,n) :
    page = requests.get("https://www.seek.com.au/jobs-in-construction?page="+str(i))
    soup = BeautifulSoup(page.content, 'html.parser')

    for a in soup.find_all('a', href=True, class_='_257MqcB'):
        print(type(a.getText()))
        print(type(a.text()))
        #list_name.append(a.text())        
        
print(len(list_name))

for i in range (0, len(list_name)-1) :
    scraperwiki.sqlite.save(unique_keys=['company_name'], data={"company_name": list_name[i]})
