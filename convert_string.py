from configuration import general_stop_words
from string import punctuation


class WorkString:
    def __init__(self, data):
        self.data = data

    def convert_string(self):
        sentence = self.data.strip()
        sentence = sentence.replace(" ", "+")
        sentence = sentence.replace("'", "+")
        sentence = sentence.replace("?", "")
        return sentence

    def remove_stop_words(self):
        address_list_sort = []
        address_list = self.data.split()
        for item in address_list:
            if item.lower() not in general_stop_words :
                address_list_sort.append(item)
        address_list_sort = address_list_sort[-3:]
        address_sort = " ".join(address_list_sort)
        return address_sort


