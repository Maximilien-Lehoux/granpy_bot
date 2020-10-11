"""call file at the wikipedia API. we get the title, the extract and the url
of the page"""
import requests
from constant import URL_WIKIPEDIA


class DataApiWikipedia:
    """the request to the API which contains the parameters"""
    def __init__(self):
        self.url = URL_WIKIPEDIA

    def get_title_page_wikipedia(self, text):
        """get the title of the wikipedia page corresponding to the
        customer input"""
        payload = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": text,
            "srlimit": 1,
        }
        try:
            response = requests.get(self.url, params=payload)
            data = response.json()
            title = data['query']['search'][0]['title']
            return title
        except (IndexError, KeyError):
            return "OpenClassrooms"

    def get_page_extract(self, page_title):
        """get the title of the wikipedia article corresponding to the
        customer entry"""
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

        response = requests.get(self.url, params=payload).json()
        return list(response['query']['pages'].values())[0]['extract']

    def get_url_page_wikipedia(self, page_title):
        """get the url of the wikipedia article corresponding
        to the customer entry"""
        payload = {
            "action": "query",
            "format": "json",
            "titles": page_title,
            "prop": "info",
            "inprop": "url",
        }
        response = requests.get(self.url, params=payload).json()
        return list(response['query']['pages'].values())[0]['fullurl']
