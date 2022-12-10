import requests
from bs4 import BeautifulSoup
import json


url = 'https://b165716.yclients.com/api/v1/book_staff/170715?datetime=&without_seances=1'
headers = {
    'authority': 'b165716.yclients.com',
    'method': 'GET',
    'path': '/api/v1/book_staff/170715?datetime=&without_seances=1',
    'scheme': 'https',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU',
    'authorization': 'Bearer gtcwf654agufy25gsadh',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/107.0.0.0 Safari/537.36',
    'cookie': 'analytics-udid=RlqBnxCZLdXtxzQm6evVEXtVUw1YBlDHFz9ZR4RY; auth=8ftokdcnkm4c5hfuidim0njatbmrtma3s32bf5gmgqcjkmj5kbiii0uavupm7k73; _ym_uid=1669973758836967157; _ym_d=1669973758; _cfuvid=ZW6.mv_gWhJ7msNf2t0BYGfjr3RMn0XLfqE7u3wYlHg-1670600637001-0-604800000; __cf_bm=wrn5C8SAINVEpcO7YSOPaIan8V7G3j81ExPm48wr0iY-1670600638-0-AWWD0sznQ2ntSlQ+mQaTunTGGacMpJ1yJEr4u5EORqr8N8zKVjfZ9ymu+hdozz7tjDva3i4WJErFriX720qjZHWGt/Orx32v5EAW7nfXgOMpF3cVAJWR76kCDvFpaMXC0IM50MFkMTFWWWpfv1vCUacnn4fYNIsfqmwuI1Aolw12Alz3vcrhSOt5DGWxMpvMYA==; _ym_isad=1; _ym_visorc=w; tracking-index=27',
    'dnt': '1',

}
req = requests.get(url, headers=headers)

src = req.text

with open('new.json', 'w') as file:
    json.dump(src, file, indent=4, ensure_ascii=False)
with open('new.html', 'w') as file:
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




