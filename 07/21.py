def size_of_dictionary(my_dict):
    """
    return an integer representing the number of items in the
    dictionary.
    """
    print len(my_dict)
    return len(my_dict)


assert size_of_dictionary({"a":"b"}) == 1
assert size_of_dictionary({"a":"b", "c": "D"}) == 2
