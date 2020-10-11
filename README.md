# GranPy Bot, le papy-robot

It's an application written in python and javascript via the flask module

## Getting started

procedure to install the application

### Prerequisites

Download and install python 3.7.0

### Installing

step by step :

"""
$ pip install -r requirements.txt
"""

Activate your virtual environnement

"""
virtualenv -p python3 env
env\Scripts\activate.bat
"""

To create "constant.py" at the root of the project and and add your api keys :

"""
KEY_API_GEOCODE = "your api key geocode"

KEY_GOOGLE_MAP = "your api key google map"

URL_WIKIPEDIA = "your api key wikipedia"
"""

to start the server :

"""
python run.py
"""

in the address : http://127.0.0.1:5000

## Running the tests

You can run tests by running the files:

"""
pytest
"""

## To configure

You can modify the list of words to delete in the configuration file

## to modify api keys

you can modify API keys with your own for professional use

## Deployment

The app is deployed on Heroku at https://granpy-bot-lehoux.herokuapp.com/

## Authors

* **Maximilien Lehoux** https://github.com/Maximilien-Lehoux?tab=repositories