import requests
import json

with open('token.txt') as f:
    token = f.readline().strip()

class YandexDisk:
    def __init__(self, token, name='new'):
        self.token = token
        self.headers = {
                "Accept": "application/json",
                "Authorization": "OAuth " + self.token
            } 
        self.params = {
                'path':name
            } 
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def create_dir(self):

        response = requests.put(url=self.url, params=self.params, headers=self.headers)
        response.raise_for_status()
        return response.status_code
    
    def get_info(self):
        result = requests.get(url=self.url, params=self.params, headers=self.headers)
        if result.status_code == 200:
            res_dict = json.loads(result.text)
            return res_dict.get('type')

if __name__ == '__main__':
    ya = YandexDisk(token)
