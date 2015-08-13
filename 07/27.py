def lotto_winner(lotto_tickets_by_person, winning_number):
    """
    given a dictionary of <string, list[int]> pairs, where
    the key is the name of the person and the value is a
    list of the lotto tickets the person has, returning the
    name of the person who has the winning number.
    """
    z=[]
    for k, v in lotto_tickets_by_person.iteritems():

        for x in v:

            if x == winning_number:
                print x
                return k
lotto_numbers = {
    "john": [15, 17, 12, 13],
    "mark": [1, 10, 19, 14],
    "tracy": [3, 4, 5]
}





assert lotto_winner(lotto_numbers, 1) == "mark"
assert lotto_winner(lotto_numbers, 4) == "tracy"
assert lotto_winner(lotto_numbers, 12) == "john"

print("it works, congrats!")
