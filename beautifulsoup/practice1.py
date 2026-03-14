
# scrapping real websites
# pip install requests


# import beautiful soup version 4 library to import beautiful soup class
from bs4 import BeautifulSoup
import requests

request_status = requests.get('https://mohamed-a-awara.github.io/tailwind-project/' , verify= False)
# print request status
print(request_status )
# 200  => request is done successfully
print('--------------------------------------------------------------')
soup = BeautifulSoup( request_status.text , 'lxml' )
h3_tages = soup.find_all('h3')
for tag in h3_tages:
    print(tag)



