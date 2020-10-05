"""get user question, convert and remove stop words"""
from configuration import general_stop_words


class WorkString:
    """allows to sort the character string entered by the customer"""
    def __init__(self, data):
        self.data = data

    def get_address_without_punctuation(self):
        """remove the punctuation and go through the "+" necessary for the
        google map api"""
        sentence = self.data
        sentence = sentence.replace("?", "")
        sentence = sentence.strip()
        sentence = sentence.replace("-", " ")
        sentence = sentence.replace(" ", "+")
        sentence = sentence.replace("'", "+")

        return sentence

    def get_address_selected(self):
        """get the keywords for the api from wikipedia"""
        address_list_sort = []
        address_list = self.data.split()
        for item in address_list:
            if item.lower() not in general_stop_words :
                address_list_sort.append(item)
        address_list_sort = address_list_sort[-3:]
        address_sort = " ".join(address_list_sort)
        return address_sort
