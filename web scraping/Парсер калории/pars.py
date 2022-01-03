from bs4.dammit import encoding_res
import requests
from bs4 import BeautifulSoup
import json
from requests.api import request

from requests.sessions import should_bypass_proxies


# url= 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
# domen= 'https://health-diet.ru'
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Accept': '*/*',
}

# req=requests.get(url, headers=headers)
# src = req.text

# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(src)                                         #Сохраняем файл

    

# soup=BeautifulSoup(src, 'lxml')
# items = soup.find_all(class_='mzr-tc-group-item-href')


# for item in items:
#     print(item.text)
# with open ('index.html',encoding='utf-8') as file:
#     src=file.read()

# soup=BeautifulSoup(src, 'lxml')
# all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
# domen= 'https://health-diet.ru'

# all_categories_dict = {}

# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = domen + item.get('href')
#     print(f"{item_text}:{item_href}")
#     all_categories_dict[item_text] = item_href


# with open("all_categories_dict", "w", encoding='utf-8') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
#             # indent - отступ в файле, без него данные будут в строку
#             # ensure_ascii - не єкрвнирует символы

with open("all_categories_dict", encoding='utf-8') as file:
    all_categories = json.load(file)                   #open file

print(all_categories)

count = 0
for category_name, category_href in all_categories.items():

    rep = [","," ", "-", "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")
    print(category_name)

    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f"data/{count}_{category_name}.html", "w", encoding='utf-8') as file:
        file.write(src)

    count +=1





