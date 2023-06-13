'''Используя парсинг данных с маркетплейса beru.ru, найдите, на сколько литров отличается общий объем холодильников
Саратов 263 и Саратов 452?
Для парсинга можно использовать зеркало страницы beru.ru с результатами для холодильников Саратов по адресу:
video.ittensive.com/data/018-python-advanced/beru.ru/'''

import requests
from bs4 import BeautifulSoup

headers = {'User=Agent': 'ittensive-python-courses/1.0 (+https://www.ittensive.com/)'}
r = requests.get('https://video.ittensive.com/data/018-python-advanced/beru.ru/', headers=headers)
html = BeautifulSoup(r.content, 'lxml')
links = html.find_all('a', {'class': '_3ioN70chUh Usp3kX1MNT _3Uc73lzxcf'})
link_263 = ''
link_452 = ''
for link in links:
    if str(link).find('Саратов 263') > -1:
        link_263 = link['href']
    if str(link).find('Саратов 452') > -1:
        link_452 = link['href']


def find_volume(link):
    r = requests.get('https://video.ittensive.com/data/018-python-advanced/beru.ru/' + link)
    html = BeautifulSoup(r.content, 'lxml')
    volume = html.find_all('span', {'class': '_112Tad-7AP'})
    return int(''.join(i for i in volume[2].get_text() if i.isdigit()))


if link_263 and link_452:
    volume_263 = find_volume(link_263)
    volume_452 = find_volume(link_452)
    diff = max(volume_263, volume_452) - min(volume_263, volume_452)
    print('Общий объем холодильников Саратов 263 и Саратов 452 отличается на', diff, 'л.')
