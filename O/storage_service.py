from __future__ import annotations
from storage import *


class StorageService:
    def __init__(self, storage: JSONStorage | YAMLStorage):
        self.storage = storage

    def get(self, key: str) -> str:
        return self.storage.get_value(key)


storageJ = StorageService(JSONStorage('data.json'))
storageY = StorageService(YAMLStorage('data.yaml'))
print(storageJ.get('username'))
print(storageY.get('username'))

