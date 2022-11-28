import os
import requests

from settings import TOKEN

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    base_host = "https://cloud-api.yandex.net:443/"


    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, file_path: str):
         """Метод получает ссылку для загрузки файла на Яндекс-диск"""
         uri = 'v1/disk/resources/upload/'
         requests_url = self.base_host + uri
         params = {'path': file_path, 'overwrite': True}
         response = requests.get(requests_url, headers=self.get_headers(),
                                params=params)
         print(response.json())
         return response.json()['href']

    def upload_to_disk(self, path_to_file, file_path):
         upload_url = self._get_upload_link(file_path)
         response = requests.put(upload_url,
                                 data=open(path_to_file, 'rb'),
                                 headers=self.get_headers())
         if response.status_code == 201:
             print("Загрузка произошла успешно")


if __name__ == '__main__':

    path_to_file = "C:\\Документы для СЭД\Порт Батуми.jpg"
    token = TOKEN
    uploader = YaUploader(token)
    uploader.upload_to_disk(path_to_file, "Порт Батуми")