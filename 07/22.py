def list_all_keys_in_dict(my_dict):
    """ print all keys in the dictionary """
    list = []
    for x in my_dict:
        print (x)
        list.append(x)
    return list

assert list_all_keys_in_dict({"a": "b"}) == ["a"]
assert list_all_keys_in_dict({"a": "b", "c": "d"}) == ["a", "c"]
