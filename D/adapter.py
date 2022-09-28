import requests
import xmltodict
from abc import ABC, abstractmethod


class Connection(ABC):
    def get_data(self):
        pass


class RequestConnection(Connection):
    def __init__(self, requests):
        self.requests = requests

    def get_data(self):
        pass


class ApiClient:
    def __init__(self, fetch: RequestConnection):
        self.fetch = fetch

    #
    def get_xml(self, url):
        response = self.fetch.requests.get(url)
        return response.text


def parse_usd(data):
    exc = data.get('exchangerates', None)
    if exc:
        return exc.get('row')[0].get('exchangerate').get('@buy')
    return None


def xml_adapter(xml):
    return dict(xmltodict.parse(xml))


if __name__ == "__main__":
    client = ApiClient(RequestConnection(requests))
    data = client.get_xml('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
    print(parse_usd(xml_adapter(data)))
