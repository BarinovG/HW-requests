from pprint import pprint
import requests

TOKEN = ''

class YaUploader:
    def __init__(self, token):
        self.token = TOKEN

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

uploader = YaUploader(token=TOKEN)
uploader.upload(disk_file_path='/Netology/Test2.txt', filename='Test2.txt')


