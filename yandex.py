import requests


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, path_to_download, file_name):
        result=self._link(path_to_download=path_to_download)
        href=result.get('href', '')
        response=requests.put(href, data=open(file_name, 'rb'))
    def _link(self, path_to_download):
        url='https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers={'Content-Type': 'application/json',
                 'Authorization': f'OAuth {self.token}'}
        params ={'path': path_to_download, 'overwrite': 'true'}
        response= requests.get(url, headers=headers, params=params)
        return response.json()