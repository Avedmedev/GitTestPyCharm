from __future__ import annotations
from storage import *


class StorageService:
    def __init__(self, storage: JSONStorage | YAMLStorage):
        self.storage = storage

    def get(self, key: str) -> str:
        return self.storage.get_value(key)


if __name__ == '__main__':
    for storage_ in [StorageService(JSONStorage('data.json')), StorageService(YAMLStorage('data.yaml'))]:
        print(storage_.get('username'))
