import requests


class DataApiWikipedia:
    """the request to the API which contains the parameters"""
    def __init__(self):
        self.url = "https://fr.wikipedia.org/w/api.php"

    def get_title_page_wikipedia(self, text):
        payload = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": text,
            "srlimit": 1,
        }
        response = requests.get(self.url, params=payload)
        data = response.json()
        title = data['query']['search'][0]['title']
        return title

    def get_page_extract(self, page_title):
        payload = {
            "action": "query",
            "format": "json",
            "titles": page_title,
            "prop": "extracts",
            "exchars": 200,
            "exintro": 0,
            "exlimit": 1,
            "explaintext": 1,
            "exsectionformat": "plain",
        }
        r = requests.get(self.url, params=payload).json()
        return list(r['query']['pages'].values())[0]['extract']

    def get_url_page_wikipedia(self, page_title):
        payload = {
            "action": "query",
            "format": "json",
            "titles": page_title,
            "prop": "info",
            "inprop": "url",
        }
        r = requests.get(self.url, params=payload).json()
        return list(r['query']['pages'].values())[0]['fullurl']
