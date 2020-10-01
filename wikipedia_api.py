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
        response = requests.get(self.url, params=payload)
        data = response.json()
        title = data['query']['search'][0]['title']
        return title

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
        r = requests.get(self.url, params=payload).json()
        return list(r['query']['pages'].values())[0]['extract']

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
        r = requests.get(self.url, params=payload).json()
        return list(r['query']['pages'].values())[0]['fullurl']


data_wikipedia = DataApiWikipedia()
example1 = data_wikipedia.get_title_page_wikipedia('gare périgueux')
print(example1)

example2 = data_wikipedia.get_page_extract(example1)
print(example2)

example3 = data_wikipedia.get_url_page_wikipedia(example2)
print(example3)