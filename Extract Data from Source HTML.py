import requests
from bs4 import BeautifulSoup

URL = 'https://theinternship.io/'
page = requests.get(URL)
page.encoding = "utf-8"
soup = BeautifulSoup(page.text, 'html.parser')

for link in soup.find_all(class_='center-logos'):
    print(link.get('src'))

