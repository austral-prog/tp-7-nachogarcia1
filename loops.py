def index_of_by_index(word, list, index):
    for index2, element in enumerate(list[index:]):
        if element == word:
            return index2 + index
    return -1


def index_of_empty(list):
    for index, element in enumerate(list):
        if element == "":
            return index
    return -1


def index_of(word, list):
    for index, element in enumerate(list):
        if element == word:
            return index
    return -1


def put(word, list):
    for index, element in enumerate(list):
        if element == "":
            list[index] = word
            return index
    return -1


def remove(word, list):
    count = 0
    for index, element in enumerate(list):
        if element == word:
            list[index] = ""
            count += 1
    return count
    return -1
