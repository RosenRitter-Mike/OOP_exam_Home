from ideck import IDeck
from card import Card
from errors import DeckCheatingError
from card_suit import CardSuit
from card_rank import CardRank

from typing import override
import random as rnd


def fair_deck(func):
    def wrapper(*args, **kwargs):
        result1 = func(*args, **kwargs)
        result2 = func(*args, **kwargs)

        print("Shuffle Result 1:", result1)
        print("Shuffle Result 2:", result2)

        if result1 != result2:
            return result1
        else:
            raise DeckCheatingError("This is not a valid deck!! Stop cheating!!")

    return wrapper


class Deck(IDeck):
    def __init__(self, shuffle=True):
        self._cards = Deck.build_deck()
        self._index = 0
        # if shuffle:
        #     self.shuffle()

    @property
    def cards(self):
        return self._cards

    @override
    @fair_deck
    def shuffle(self):
        # rnd.shuffle(self._cards)
        new_deck = rnd.sample(self._cards, len(self._cards))
        self._cards = new_deck
        return self._cards

    @override
    def draw(self) -> Card:
        return self._cards.pop()

    @override
    def add_card(self, new_card: Card):
        self._cards.append(new_card)

    @override
    def __len__(self):
        return len(self._cards)

    @override
    def __getitem__(self, idx):
        if not isinstance(idx, int):
            raise TypeError("index of card can only be int")
        return self._cards[idx]

    @override
    def __iter__(self):
        return self

    @override
    def __next__(self):
        if self._index >= len(self._cards):
            self._index = 0
            raise StopIteration
        value = self._cards[self._index]
        self._index += 1
        return value

    @classmethod
    def build_deck(cls) -> list[Card]:
        new_deck = []
        for suit in CardSuit:
            for rank in CardRank:
                card = Card(suit, rank)
                new_deck.append(card)

        return new_deck
