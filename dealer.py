# Import pyDealer library
import pydealer as pd
# Import CardDeck class
from cardDeck import CardDeck

# Inherit the card deck from the CardDeck class
class Dealer(CardDeck):
    # Create a new empty hand for the dealer
    def __init__(self):
        self.hand = pd.Stack()

    # Give two cards to the dealer
    def startingHand(self):
        self.hand += CardDeck.deck.deal(2)
        print(self.hand)

y = Dealer()
x = Dealer()
y.startingHand()
x.startingHand()

print(y)