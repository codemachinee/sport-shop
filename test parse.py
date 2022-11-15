import requests
from bs4 import BeautifulSoup
import json


url = 'https://ccm.ru/'
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/107.0.0.0 Safari/537.36'
}
req = requests.get(url, headers=headers)

src = req.text

with open('ccm.html', 'w') as file:
    file.write(src)

with open('ccm.html') as file:
    src = file.read()
categories_dict = {}
general_menu = []
under_category = []
soup = BeautifulSoup(src, 'lxml')
items = soup.findAll(class_='menu-link')
for item in items:
    general_menu.append(item.text)
    categories_dict['general_menu'] = general_menu
items = soup.findAll(class_='top-submenu')
for e in range(0, 8):
    under_category = []
    li = items[e].find_all('li')
    for a in li:
        under_category.append(a.text.replace('\n', '').replace('\t', '').strip())
    categories_dict[(general_menu[e])] = under_category
    with open('categories_dict.json', 'w') as file:
        json.dump(categories_dict, file, indent=4, ensure_ascii=False)




