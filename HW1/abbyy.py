#   OTM2NzJmOTktNzRkYy00NzQyLTg5YTctZWNjNWU3ZWY0YzRiOjA2NzcwYzMyNWFmZDQ4NjQ4NDE3ZDRhNTA0ZmY4N2Y3
import json
import requests
from pprint import pprint


url = 'https://developers.lingvolive.com/'
method = 'api/v1.1/authenticate'
api_key = 'OTM2NzJmOTktNzRkYy00NzQyLTg5YTctZWNjNWU3ZWY0YzRiOjA2NzcwYzMyNWFmZDQ4NjQ4NDE3ZDRhNTA0ZmY4N2Y3'

headers = {
    'Authorization': f'Basic {api_key}'
}

response = requests.post(f'{url}{method}',headers=headers)
token = response.text

print(token)