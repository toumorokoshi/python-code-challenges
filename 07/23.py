def number_of_keys_with_foo_in_name(my_dict):
    """ return an integer, with the number of keys with the string "foo" in them. """
    pass



test_1 = {
    "foo": "bar",
    "foo2": "bar2",
    "barfoo": "bar3",
    "oogles": "bar4",
    "oofbar": "bar5"
}
assert number_of_keys_with_foo_in_name(test_1) == 3

test_2 = {
    "hobo": "mobo",
    "robo": "cop"
}

assert number_of_keys_with_foo_in_name(test_2) == 0

print("it works, congrats!")
