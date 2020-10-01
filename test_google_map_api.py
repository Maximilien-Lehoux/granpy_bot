import urllib.request
from google_map_api import DataApi

example_latitude = '45.18735239999999'
example_longitude = '0.7077530999999999'
example_address = 'Gare de Perigueux, 11 Rue Denis Papin, 24000 Périgueux, France'


def test_http_return_latitude(monkeypatch):
    results = example_latitude

    def mockreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    example = DataApi('Gare périgueux')
    assert example.get_latitude() == results


def test_http_return_longitude(monkeypatch):
    results = example_longitude

    def mockreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    example = DataApi('Gare périgueux')
    assert example.get_longitude() == results


def test_http_return_address_complete(monkeypatch):
    results = example_address

    def mockreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    example = DataApi('Gare périgueux')
    assert example.get_address_complete() == results
