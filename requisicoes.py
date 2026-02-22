import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')
site = BeautifulSoup(response.content, 'html.parser')

posts = site.find_all('div', class_='feed-post-body')

for post in posts:
    img = post.find('img')
    if img:
        print(img.get('alt', 'No alt found'))

