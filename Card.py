SUITS = ["DIAMONDS", "SPADES", "HEARTS", "CLUBS"]
VALUES = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]


class Card:

    # Card constructor
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

        # Returns the suit of the card.
    def suit(self):
        return self.suit

        # Returns the value of the card.
    def value(self):
        return self.value


class Deck:

        # Creates a sorted deck of playing cards. 13 values, 4 suits.
    def __init__(self):
        Card()

        # Returns the number of Cards in the Deck
    def num_cards(self):

        # Shuffles the deck of cards.
    def shuffle(self):

        # Returns the top Card in the deck, then puts it back.
    def peek(self):

        # Draws and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self):

        # Adds the input card to the deck. If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card):

        # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self):
        for c in Card.suit():
            print(c)
