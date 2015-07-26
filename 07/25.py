def sum_of_values_with_foo_in_key_name(my_dict):
    """
    given a dictionary of <string, int> mappings,
    return the sum of all value for keys which have "foo"
    in them.
    """
    pass


test_1 = {
    "foo": 0,
    "foo2": 65,
    "barfoo": -10,
    "oogles": 23,
    "oofbar": -10
}

assert sum_of_values_with_foo_in_key_name(test_1) == 55

test_2 = {
    "hobo": -12,
    "robo": 25
}

assert sum_of_values_with_foo_in_key_name(test_2) == 0

print("it works, congrats!")
