import requests
from bs4 import BeautifulSoup
import scraperwiki

list_name = []
list_link = []
list_date = []
    
#Loop to get the n first pages
n = 3
for i in range (1,100) :
    page = requests.get("https://www.seek.com.au/jobs-in-construction?daterange=7&page="+str(i))
    soup = BeautifulSoup(page.content, 'html.parser')
    
    
    for a in soup.find_all('a', href=True, class_='_3FrNV7v _8LyaGjS _3PZrylH _2heRYaN E6m4BZb'):
        print(a.getText())
        list_date.append(a.getText()) 
    
    for a in soup.find_all('a', href=True, class_='_1EkZJQ7'):
        print(a.getText())
        list_link.append("https://www.seek.com.au/"+a['href'])
    

    for a in soup.find_all('a', href=True, class_='_257MqcB'):
        list_name.append(a.getText())
        print(a.getText())

 
      
print(len(list_link))        
print(len(list_name))
print(len(list_date))

for i in range (0, len(list_name)-1) :
    scraperwiki.sqlite.save(unique_keys=['link'], data={"link": list_link[i], "date": list_date[i], "company_name": list_name[i]})
