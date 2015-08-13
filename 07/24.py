def sum_all_values(my_dict):
    """
    given a dictionary of <string, int> mappings,
    return the sum of all the values.
    """
    return (sum(my_dict.values()))


test_1 = {
    "ben": 4,
    "caro": 10,
    "john": 15,
    "mike": 0
}

assert sum_all_values(test_1) == 29

test_2 = {
    "paul": 10,
    "ken": -5,
    "tru": 12
}

assert sum_all_values(test_2) == 17

print("it works, congrats!")
