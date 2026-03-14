
# into terminal write:
# pip install beautifulsoup4
# pip install lxml              ( make scrapping faster )


from bs4 import BeautifulSoup
# open "ttargeted file" in the "read" mode and save it in a variable called "html_file"
# with = close file automatically after finish
with open('./beautifulsoup/index.html' , 'r') as html_file:
    content = html_file.read()
    # print(content)
    print('------------------------------------------------------------')
    # show all html tages
    soup = BeautifulSoup(content , 'lxml')
    print(soup.prettify())
    print('------------------------------------------------------------')
    # show only the first picked tages 
    tag = soup.find('h2')
    print(tag)
    print('------------------------------------------------------------')
    # print the all picked tages
    tags = soup.find_all('h2')
    for i in range (len(tags)):
        print(tags[i])
    print('------------------------------------------------------------')
    # print all grapped tages filtered by class_ name
    filtered_tages = soup.find_all('div' , class_ = 'class1')
    for tag in filtered_tages:
        print(tag)
    print('------------------------------------------------------------')
    card_tag = soup.find_all('div' , class_ = 'class1')
    for div in card_tag:
        print(f"course: {div.h4.text}    cost: {div.h5.text}")
