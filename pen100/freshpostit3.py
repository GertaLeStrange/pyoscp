#!/usr/bin/python3
#postit.py

#!/usr/bin/python3
#web-client2.py

import requests
from bs4 import BeautifulSoup


url = 'http://192.168.69.68:8080/about.html'
url2 = 'http://192.168.69.68:8080/login-3/index.php'


reqq = requests.get(url)

#print(reqq.content)

soup = BeautifulSoup(reqq.text, 'lxml')
#for row in soup.findAll('table')[0].tbody.findAll('tr'):
#    first_column = row.findAll('th')[0].contents
#    print(first_column)
table = soup.find('table').tbody
print (table.measure)
for row in table.find_all('tr'):
    bits = str(row.find_all('td')[2].contents)[2:-2]
    print (bits)
    info = {'username': bits, 'password': 'test'}
    post = requests.post(url2, data = info)
    soup = BeautifulSoup(post.text)
    print (soup.div)


#    print (post.text.div)


#print(table)
#print(soup.table.tr.prettify())


#tables = soup.find_all('table')
#print (tables)



#with open("test2.bin", "wb") as file:
#    file.write(binary.content)

#print(post.text)
