from deck import Deck
from errors import DeckCheatingError

deck = Deck()
print(f"Deck size: {len(deck)}")

try:
    new_deck = deck.shuffle()
    print("Deck shuffled successfully")
except DeckCheatingError:
    print("Cheating detected! Deck not shuffled properly!")

card1 = deck.draw()
card2 = deck.draw()
print(f"Drawn cards: {card1}, {card2}")
print(f"Deck size after drawing: {len(deck)}")

print("\nAccessing cards directly by index:")
for i in range(5):
    print(f"Card at index {i}: {deck[i]}")

print("\nIterating through all cards in the deck:")
for card in deck:
    print(card)