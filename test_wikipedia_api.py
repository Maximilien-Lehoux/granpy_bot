"""test the class and the methods of the wikipedia_api file"""
import urllib.request
from app.wikipedia_api import DataApiWikipedia

TITLE_PAGE = 'Gare de Périgueux'
EXTRACT_PAGE = 'La gare de Périgueux est une gare ferroviaire française des ' \
               'lignes de Coutras à Tulle et de Limoges-Bénédictins à ' \
               'Périgueux, située dans le quartier Saint-Martin à proximité ' \
               'du centre ville de Périgueux…'
URL_PAGE = 'https://fr.wikipedia.org/wiki/La_gare_de_P%C3%A9rigueux_est_' \
           'une_gare_ferroviaire_fran%C3%A7aise_des_lignes_de_Coutras_' \
           '%C3%A0_Tulle_et_de_Limoges-B%C3%A9n%C3%A9dictins_%C3%A0_' \
           'P%C3%A9rigueux,_situ%C3%A9e_dans_le_quartier_Saint-Martin_' \
           '%C3%A0_proximit%C3%A9_du_centre_ville_de_P%C3%A9rigueux%E2%80%A6'


def test_http_return_title_page(monkeypatch):
    """test obtaining the title with the wikipedia api"""
    results = TITLE_PAGE

    def mockreturn():
        """use a mock to simulate the api call"""
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    example = DataApiWikipedia()
    assert example.get_title_page_wikipedia('Gare périgueux') == results


def test_http_return_extract_page(monkeypatch):
    """test obtaining the article with the wikipedia api"""
    results = EXTRACT_PAGE

    def mockreturn():
        """use a mock to simulate the api call"""
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    example = DataApiWikipedia()
    assert example.get_page_extract(TITLE_PAGE) == results


def test_http_return_url_page(monkeypatch):
    """test obtaining the url with the wikipedia api"""
    results = URL_PAGE

    def mockreturn():
        """use a mock to simulate the api call"""
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    example = DataApiWikipedia()
    assert example.get_url_page_wikipedia(EXTRACT_PAGE) == results
