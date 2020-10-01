import urllib.request

from app.wikipedia_api import DataApiWikipedia

title_page = 'Gare de Périgueux'
extract_page = 'La gare de Périgueux est une gare ferroviaire française des ' \
               'lignes de Coutras à Tulle et de Limoges-Bénédictins à ' \
               'Périgueux, située dans le quartier Saint-Martin à proximité ' \
               'du centre ville de Périgueux…'
url_page = 'https://fr.wikipedia.org/wiki/La_gare_de_P%C3%A9rigueux_est_' \
           'une_gare_ferroviaire_fran%C3%A7aise_des_lignes_de_Coutras_' \
           '%C3%A0_Tulle_et_de_Limoges-B%C3%A9n%C3%A9dictins_%C3%A0_' \
           'P%C3%A9rigueux,_situ%C3%A9e_dans_le_quartier_Saint-Martin_' \
           '%C3%A0_proximit%C3%A9_du_centre_ville_de_P%C3%A9rigueux%E2%80%A6'


def test_http_return_title_page(monkeypatch):
    results = title_page

    def mockreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    example = DataApiWikipedia()
    assert example.get_title_page_wikipedia('Gare périgueux') == results


def test_http_return_extract_page(monkeypatch):
    results = extract_page

    def mockreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    example = DataApiWikipedia()
    assert example.get_page_extract(title_page) == results


def test_http_return_url_page(monkeypatch):
    results = url_page

    def mockreturn(request):
        return results

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    example = DataApiWikipedia()
    assert example.get_url_page_wikipedia(extract_page) == results
