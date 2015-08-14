class Deck(object):
    """
    This class represents a deck. the __init__ method takes in a list
    of the cards in the deck, in order from top to bottom.

    Deck has a method draw() that returns the card at the current top
    of the deck, and removes the top card from the deck.
    """
    pass


ACE_OF_SPADES = "ace of spades"
KING_OF_HEARTS = "king of hearts"
FIVE_OF_CLUBS = "five of clubs"
deck = Deck([ACE_OF_SPADES, KING_OF_HEARTS, FIVE_OF_CLUBS])
assert deck.draw() == ACE_OF_SPADES
assert deck.draw() == KING_OF_HEARTS
assert deck.draw() == FIVE_OF_CLUBS
