from app.convert_string import WorkString

sentence = "Salut GrandPy ! Est-ce que tu connais l'adresse de la gare de Périgueux ?"
sentence_without_punctuation = "Salut+GrandPy+!+Est+ce+que+tu+connais+l+adresse+de+la+gare+de+Périgueux"
sentence_address_selected = "connais gare Périgueux"


def test_get_sentence():
    address = WorkString(sentence)
    assert address.data == sentence


def test_get_address_without_punctuation():
    address = WorkString(sentence)
    assert address.get_address_without_punctuation() == sentence_without_punctuation


def test_get_address_selected():
    address = WorkString(sentence)
    assert address.get_address_selected() == sentence_address_selected


