import requests
# from convert_string import address_converted
from configuration import secret_key

# URL_GENERAL = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(address_converted, secret_key)


class DataApi:
    """the request to the API which contains the parameters"""
    def __init__(self, address):
        self.url = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}".format(address, secret_key)
        self.response = requests.get(self.url)
        self.data_location = self.response.json()["results"][0]["geometry"]["location"]

    def latitude(self):
        data_latitude = self.data_location["lat"]
        data_latitude = str(data_latitude)
        return data_latitude

    def longitude(self):
        data_longitude = self.data_location["lng"]
        data_longitude = str(data_longitude)
        return data_longitude





