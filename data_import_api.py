'''Выполните запрос к API и узнайте долготу точки на карте (Point) для города Самара.'''

import json
import requests

r = requests.get(
    "https://geocode-maps.yandex.ru/1.x/?geocode=Самара&apikey=3f355b88-81e9-4bbf-a0a4-eb687fdea256&format=json")
geo = json.loads(r.content)
print("Долгота у точки на карте для Самары:",
      geo['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(" ")[0])
