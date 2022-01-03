from bs4.builder import TreeBuilderRegistry
from bs4.element import SoupStrainer
from lxml import html
import requests
from bs4 import BeautifulSoup


url='https://auto.ria.com/uk/legkovie/?page=1'
response = requests.get(url)
soup= BeautifulSoup(response.text , 'lxml')

items= soup.find('section', class_='ticket-item').find('span', class_='blue bold').text


print(items)