

# import libraries
from bs4 import BeautifulSoup
import requests

website = requests.get('https://realpython.github.io/fake-jobs/')
# to print request status
print(f'request status: {website}')

soup = BeautifulSoup(website.text , 'lxml')

card_content = soup.find_all('div' , class_ = 'card-content')
for job in card_content:
    jobName = job.find('h2').text.strip()
    companyName = job.find('h3').text.strip()
    companyLocation = job.find('p' , class_ = 'location').text.strip()


    print(f'''
    job Name         : {jobName}
    company Name     : {companyName}
    company Location : {companyLocation}
    ''')

