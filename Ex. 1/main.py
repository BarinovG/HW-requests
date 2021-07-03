import requests
from pprint import pprint

super_heroes = ['Thanos', 'Hulk', 'Captain_America']
API_KEY = '2619421814940190'

def best_intelligence(heroes):
    url_pack = []
    intelligence_dict = {}
    uri = 'https://superheroapi.com/api/'
    acces_tokken = API_KEY
    max = 0

    #Собираем юрлы для запросов
    for hero in heroes:
        uri2 = '/search/' + hero
        full_url = uri + acces_tokken + uri2
        url_pack.append(full_url)

    #Делаем запросы и собираем в словарь Имя - показатель интеллекта
    for url in url_pack:
        timeout = 5
        res = requests.get(url=url, timeout=timeout)
        name = res.json()["results-for"]
        intelligence = int(res.json()["results"][0]['powerstats']['intelligence'])
        intelligence_dict[name] = intelligence

    #Выводим лучший показатель
    for max_int in intelligence_dict.items():
        if max_int[1] > max:
            max = max_int[1]
            better_stats = max_int[0]
    print(f'The greatest intelligence ({max} points) has {better_stats}! Сongratulations!!!')

best_intelligence(super_heroes)

