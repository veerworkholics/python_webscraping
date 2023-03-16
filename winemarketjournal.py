import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://www.winemarketjournal.com/"

r = requests.get(URL)
#soup = bs(r.content, "html5lib")
soup = bs(r.content, "html.parser")

devices=[]
# table = soup.find('div', attrs = {'_1AtVbE col-12-12'}) 

res = soup.title
# print(soup)
# print(soup.get_text())
print(soup.prettify())
   
# for row in soup.findAll('div',attrs = {'class':'_13oc-S'}):
#     device = {}
#     device['url'] = row.a['href']
#     device['img'] = row.img['src']
#     device['alt_text'] = row.img['alt']
#     devices.append(device)
    
# filename = 'flipkart_csvfile.csv'
# with open(filename, 'w', newline='') as f:
#     w = csv.DictWriter(f,['url','img','alt_text'])
#     w.writeheader()
#     for device in devices:
#         w.writerow(device)
# print("Successfully csv file generated")