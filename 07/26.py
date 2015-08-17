def calculate_mana_cost(mana_costs):
    """
    given a dictionary of <string, int>
    mappings, where string == color and
    int == the amount of that color, give
    the total converted mana cost.

    if the color isn't one of:

        * white
        * blue
        * black
        * green
        * red
        * colorless

    ignore that value in the cost
    """
    z = 0
    for k,v in mana_costs.iteritems():
        if 'white' in k:
            z += v
        elif 'blue' in k:
            z += v
        elif 'black' in k:
            z += v
        elif 'green' in k:
            z += v
        elif 'red' in k:
            z += v
        elif 'colorless' in k:
            z += v

    return z
verdant_force = {
    "green": 3,
    "colorless": 5
}

assert calculate_mana_cost(verdant_force) == 8

sliver_queen = {
    "green": 1,
    "red": 1,
    "blue": 1,
    "white": 1,
    "black": 1
}

assert calculate_mana_cost(sliver_queen) == 5

card_misprint = {
    "red": 5,
    "groon": 2,
    "colorless": 3
}

assert calculate_mana_cost(card_misprint) == 8

print("it works, congrats!")
