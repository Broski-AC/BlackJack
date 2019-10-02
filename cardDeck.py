# Import pydealer
import pydealer as pd

# Create a new class that Dealer and Player can inherit from, to ensure that all cards come from the same deck
class CardDeck:
    deck = pd.Deck(rebuild=True, re_shuffle = True)
    deck.shuffle()