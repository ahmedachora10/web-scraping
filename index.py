import requests
from bs4 import BeautifulSoup as BSoup
from itertools import zip_longest
import csv
import  os
import json


path = '/home/ahmedachfakay/Desktop/python-web-scraping/'
url = 'https://mostaql.com/projects?category=development&skills=php&budget_max=10000&sort=latest'

def page_parser(url):
    # get web page Html
    page = requests.get(url)
    content = page.content
    # Parse Html Content
    return BSoup(content, 'lxml')

# Store Page Html Content in data Var
data = page_parser(url)

# Get Titles
titles = data.find_all('h5', {'class': 'mrg--bt-reset'})

# Init Var of type list
titles_content = {}
counter = 1

# Store Title Content in titles_content
for title in titles:
    keywords = title.text.split(' ')

    for keyword in keywords:
        keyword = keyword.strip('\n')
        # Check If Keyword Pushed to Dictionary or Not
        if titles_content.get(keyword) is None:
            titles_content.setdefault(keyword, counter)
        else:
            counter += 1
            titles_content[keyword] = counter

json_data = json.dumps(titles_content,ensure_ascii=False).encode('utf8')

with open(path + 'data/keywords.json', 'w+') as json_file:
    json_file.writelines(json_data.decode())
    
# print(titles_content)