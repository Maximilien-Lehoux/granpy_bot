import requests


class DataApi:
    """the request to the API which contains the parameters"""
    def __init__(self, address):
        self.url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(address, secret_key)
        self.response = requests.get(self.url)
        self.data_location = \
            self.response.json()["results"][0]["geometry"]["location"]

    def get_latitude(self):
        """get latitude from geocode api"""
        data_latitude = self.data_location["lat"]
        data_latitude = str(data_latitude)
        return data_latitude

    def get_longitude(self):
        """get longitude from geocode api"""
        data_longitude = self.data_location["lng"]
        data_longitude = str(data_longitude)
        return data_longitude
