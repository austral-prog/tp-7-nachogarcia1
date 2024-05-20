
def enumerate_list(colors):
    newlist = []
    index = 0
    for element in colors:
        if len(element) > 0:
            newlist.append(f"{index}. {element}")
            index += 1
    return newlist


def enumerate_backwards(colors):
    newlist2 = []
    index2 = 0
    for element in colors:
        if len(element) > 0:
            newlist2.append(f"{index2}. {element [::-1]}")
            index2 += 1
    return newlist2


print(enumerate_list(colors))
print(enumerate_backwards(colors))
