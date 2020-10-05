"""test the class and the methods of the google_map_api file"""
import urllib.request
from app.google_map_api import DataApi

EXAMPLE_LATITUDE = '45.18735239999999'
EXAMPLE_LONGITUDE = '0.7077530999999999'
EXAMPLE_ADDRESS = 'Gare de Perigueux, 11 Rue Denis Papin, 24000 Périgueux, ' \
                  'France'


def test_http_return_latitude(monkeypatch):
    """test obtaining the latitude with the geocode api of google map"""
    results = EXAMPLE_LATITUDE

    def mockreturn():
        """use a mock to simulate the api call"""
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    example = DataApi('Gare périgueux')
    assert example.get_latitude() == results


def test_http_return_longitude(monkeypatch):
    """test obtaining the longitude with the geocode api of google map"""
    results = EXAMPLE_LONGITUDE

    def mockreturn():
        """use a mock to simulate the api call"""
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    example = DataApi('Gare périgueux')
    assert example.get_longitude() == results


def test_http_return_address_complete(monkeypatch):
    """test obtaining the address complete with the geocode api of google
    map"""
    results = EXAMPLE_ADDRESS

    def mockreturn():
        """use a mock to simulate the api call"""
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    example = DataApi('Gare périgueux')
    assert example.get_address_complete() == results
