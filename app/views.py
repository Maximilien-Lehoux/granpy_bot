from flask import Flask, render_template, request
from flask_restful import reqparse

from convert_string import WorkString
from google_map_api import DataApi
from wikipedia_api import DataApiWikipedia

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/latitude_ajax', methods=['Get', 'POST'])
def latitude_ajax():
    value = request.form.get('data')
    address_converted = WorkString(value)
    address_converted = address_converted.convert_string()
    api_geocode = DataApi(address_converted)
    latitude = api_geocode.latitude()
    return latitude


@app.route('/longitude_ajax', methods=['Get', 'POST'])
def longitude_ajax():
    value = request.form.get('data')
    address_converted = WorkString(value)
    address_converted = address_converted.convert_string()
    api_geocode = DataApi(address_converted)
    longitude = api_geocode.longitude()
    return longitude


@app.route('/wikipedia_article', methods=['Get', 'POST'])
def wikipedia_article():
    value = request.form.get('data')
    address_converted = WorkString(value)
    address_converted = address_converted.remove_stop_words()
    item_wikipedia = DataApiWikipedia()
    title_wikipedia = item_wikipedia.get_title_page_wikipedia(address_converted)
    extract_wikipedia = item_wikipedia.get_page_extract(title_wikipedia)
    return extract_wikipedia


@app.route('/wikipedia_url', methods=['Get', 'POST'])
def wikipedia_url():
    value = request.form.get('data')
    address_converted = WorkString(value)
    address_converted = address_converted.remove_stop_words()
    item_wikipedia = DataApiWikipedia()
    title_wikipedia = item_wikipedia.get_title_page_wikipedia(address_converted)
    url_wikipedia = item_wikipedia.get_url_page_wikipedia(title_wikipedia)
    return url_wikipedia



