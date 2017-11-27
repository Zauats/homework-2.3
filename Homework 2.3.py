import json
from pprint import pprint
import chardet
def encoding_definition(file_name):
    with open(file_name, "rb") as f:
        data = f.read()
        result = chardet.detect(data)
        return result['encoding']


def pogramm_for_one_file(file_name):
    with open(file_name, encoding = encoding_definition(file_name)) as f:
        json_open = json.load(f)

        file_list = list()
        for list_element in json_open['rss']['channel']['items']:
            file_list.extend(list_element['description'].split(" "))

        word_list = list()
        for word in file_list:
            if len(word) > 6:
                word_list.append(word)



        words_dictionary = dict()
        for list_element in word_list:
            words_dictionary[list_element] = 0

        for list_element in word_list:
            words_dictionary[list_element] += 1


        file_list.clear()
        for words, quantity in words_dictionary.items():
            if len(file_list) < 10 :
                file_list.append(quantity)
            else:
                for number in file_list:
                    if quantity > number:
                        file_list.remove(number)
                        file_list.append(quantity)
                        break

        top_words_list = list()
        for number in file_list:
            for word, quantity in words_dictionary.items():
                if quantity == number and word not in top_words_list:
                    top_words_list.append(word)


        print(top_words_list)



pogramm_for_one_file("newsafr.json")
pogramm_for_one_file("newsfr.json")
pogramm_for_one_file("newsit.json")