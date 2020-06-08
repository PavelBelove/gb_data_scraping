# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.

import json
import requests
from pprint import pprint



def get_repos(username):
    
    # url для запроса
    url = f"https://api.github.com/users/{username}/repos"
    # Запрос
    user_data = requests.get(url).json()
    #  Можно было записывать файл все данные, но решил оставить только названия и ссылки на репозитории.
    repos_lst = []
    for repo in user_data:
        repos_lst.append({'name':repo['name'], 'url':repo['url']})       

    return repos_lst


def make_user_repos_json(username):

    with open(f"{username}_repos.json", "w") as write_file:
        json.dump(get_repos(username), write_file)


username = 'PavelBelove'
make_user_repos_json(username)
pprint(f'{username} создал {len(get_repos(username))} репозиториев:')  
pprint(get_repos(username))  




