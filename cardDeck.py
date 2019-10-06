# Import pydealer
import pydealer as pd

# Create a new class that Dealer and Player can inherit from, to ensure that all cards come from the same deck
class CardDeck:
    deck = pd.Deck(rebuild=True, re_shuffle = True)
    deck.shuffle()

    # Define a new rank dictionary
    new_ranks = {
        "values": {
            "Ace": 1,
            "King": 10,
            "Queen": 10,
            "Jack": 10,
            "10": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2,
        }
    }

    # Create a discard pile
    discardPile = pd.Stack()

    # Add cards to discard pile
    def addToDiscard(self, cards):
        self.discardPile.add(cards)
    
