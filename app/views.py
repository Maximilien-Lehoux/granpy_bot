"""routes file to html file"""
from flask import Flask, render_template, request

from app.convert_string import WorkString
from app.google_map_api import DataApi
from app.wikipedia_api import DataApiWikipedia

app = Flask(__name__)


@app.route('/')
def homepage():
    """return the html file"""
    return render_template('homepage.html')


@app.route('/address_complete', methods=['POST'])
def address_complete_ajax():
    """return the full address of the client's request in ajax"""
    value = request.form.get('data')
    address_converted = WorkString(value)
    address_converted = address_converted.get_address_without_punctuation()
    api_geocode = DataApi(address_converted)
    address_complete = api_geocode.get_address_complete()
    return address_complete


@app.route('/latitude_ajax', methods=['POST'])
def latitude_ajax():
    """return the latitude of the client's request in ajax"""
    value = request.form.get('data')
    address_converted = WorkString(value)
    address_converted = address_converted.get_address_without_punctuation()
    api_geocode = DataApi(address_converted)
    latitude = api_geocode.get_latitude()
    print(latitude)
    return latitude


@app.route('/longitude_ajax', methods=['POST'])
def longitude_ajax():
    """return the longitude of the client's request in ajax"""
    value = request.form.get('data')
    address_converted = WorkString(value)
    address_converted = address_converted.get_address_without_punctuation()
    api_geocode = DataApi(address_converted)
    longitude = api_geocode.get_longitude()
    print(longitude)
    return longitude


@app.route('/wikipedia_article', methods=['POST'])
def wikipedia_article():
    """return the wikipedia's article of the client's request in ajax"""
    value = request.form.get('data')
    address_converted = WorkString(value)
    address_converted = address_converted.get_address_selected()
    item_wikipedia = DataApiWikipedia()
    title_wikipedia = item_wikipedia.get_title_page_wikipedia\
        (address_converted)
    extract_wikipedia = item_wikipedia.get_page_extract(title_wikipedia)
    print(address_converted)
    print(title_wikipedia)
    return extract_wikipedia


@app.route('/wikipedia_url', methods=['POST'])
def wikipedia_url():
    """return the url's article of the client's request in ajax"""
    value = request.form.get('data')
    address_converted = WorkString(value)
    address_converted = address_converted.get_address_selected()
    item_wikipedia = DataApiWikipedia()
    title_wikipedia = item_wikipedia.get_title_page_wikipedia\
        (address_converted)
    url_wikipedia = item_wikipedia.get_url_page_wikipedia(title_wikipedia)
    return url_wikipedia
