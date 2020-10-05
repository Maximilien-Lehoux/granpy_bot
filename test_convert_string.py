"""test the class and the methods of the convert_string.py file"""
from app.convert_string import WorkString

SENTENCE = "Salut GrandPy ! Est-ce que tu connais l'adresse de la gare de " \
           "Périgueux ?"
SENTENCE_WITHOUT_PUNCTUATION = "Salut+GrandPy+!+Est+ce+que+tu+connais+l+" \
                               "adresse+de+la+gare+de+Périgueux"
SENTENCE_ADDRESS_SELECTED = "connais gare Périgueux"


def test_get_sentence():
    """test if we retrieve user data"""
    address = WorkString(SENTENCE)
    assert address.data == SENTENCE


def test_get_address_without_punctuation():
    """test if we retrieve user data without punctuation"""
    address = WorkString(SENTENCE)
    assert address.get_address_without_punctuation() == \
           SENTENCE_WITHOUT_PUNCTUATION


def test_get_address_selected():
    """test if we retrieve user data without stop words"""
    address = WorkString(SENTENCE)
    assert address.get_address_selected() == SENTENCE_ADDRESS_SELECTED
