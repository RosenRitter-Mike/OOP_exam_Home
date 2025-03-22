from card import Card
from card_suit import CardSuit
from card_rank import CardRank


def build_deck() -> list[Card]:
    new_deck = []
    for suit in CardSuit.value:
        for rank in CardRank.value:
            card = Card(suit, rank)
            new_deck.append(card)

    return new_deck
