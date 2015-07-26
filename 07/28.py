def all_sliver_users(card_names_by_person):
    """
    given a dictionary of <string, list[string]> pairs,
    mapping a user to all of the card names that user owns,
    return a list of all users who own a card with "sliver" in
    the name.
    """
    return [
        k for k, v in card_names_by_person.items() if
        any(["sliver" in c for c in v])
    ]


test = {
    "calciumcrusader": ["flying sliver", "muscle sliver"],
    "toumorokoshi": ["verdant force", "beast of burden"],
    "chrono": ["suicide goblin", "clear sliver"],
    "tidus": ["pacifism", "counterspell"]
}

# just an fyi, a set is a data structure that is like a list, but only
# allows unique values, and is order independent.
assert set(all_sliver_users(test)) == set(["calciumcrusader", "chrono"])

print("it works, congrats!")
