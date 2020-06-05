# Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, 
# пройдя авторизацию. Ответ сервера записать в файл.

import json
import requests
from pprint import pprint

# Очень много времени убил на попытки подключиться к API ABBYY lingvo. Согласно документации, в ответ на пост запрос на
# https://developers.lingvolive.com/api/v1/authenticate?Authorization=Basic OTM2NzJmOTktNzRkYy00NzQyLTg5YTctZWNjNWU3ZWY0YzRiOjA2NzcwYzMyNWFmZDQ4NjQ4NDE3ZDRhNTA0ZmY4N2Y3
# должен получить токен, но постоянно получаю 401. 

# Время, к сожалению, ограничено, поэтому подключусь к API попроще.



params = {
    'token': '6FpCIZY0btmSe4NjtbVpROlhFXk3E6Ix2kLUUzLP',
    'query': 'rain',
}

url = f'https://freesound.org/apiv2/search/text/'


response = requests.get(url, params=params)

with open(f'rain.json', 'wb') as write_file:
    write_file.write(response.content)

pprint(response.json())
