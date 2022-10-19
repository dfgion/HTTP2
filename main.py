from yandex import YaUploader
from os import path
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_download='/netology/test.txt'
    token = ''
    uploader = YaUploader(token)
    file_name='test.txt'
    uploader.upload(path_to_download, file_name)
