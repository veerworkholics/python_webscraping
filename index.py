import requests
from bs4 import BeautifulSoup
 
# GET request
r = requests.get('https://www.flipkart.com/mobiles-accessories/mobiles/pr?sid=tyy,4io&q=one+plus+&otracker=categorytree')
 
# check status code for response received
# check success code - 200
# print(r)
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

#find title
res = soup.title

# print(res.get_text())
# print(soup.title)
# print(soup.prettify())
# print(soup.prettify())

# Finding by id
s = soup.find('div', id= 'TABGJ6XUEHV8KQVX')
#  print(s)
# Getting the leftbar
leftbar = s.find('div', class_='_2kHMtA')
 
# All the li under the above ul
content = leftbar.find_all('div')

print(content)

