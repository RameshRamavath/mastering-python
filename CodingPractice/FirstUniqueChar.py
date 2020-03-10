# given an string - print the index of first unique or non-repeating Character - if not found return -1


from collections import OrderedDict

def getFirstUniqueChar(input_str):
    res_dict = OrderedDict()
    index = 0
    for ch in input_str:
        if res_dict.has_key(ch):
            res_dict.get(ch).append(index)
        else:
            indexes = list()
            indexes.append(index)
            res_dict.setdefault(ch, indexes)
        index += 1

    # iterate over dict elements and check first key with value size = 1

    for key, value in res_dict.iteritems():
        if len(value) == 1:
            return value[0]
    return -1


if __name__ == '__main__':

    my_string = "abbac"
    my_string2 = "love"
    print getFirstUniqueChar(my_string)
    print getFirstUniqueChar(my_string2)

    dict = OrderedDict()
    dict['name'] = 'Ramesh'
    dict['age'] = 26
    dict['place'] = 'Pune'

    print dict.get('name')