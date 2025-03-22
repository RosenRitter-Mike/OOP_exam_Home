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

        # print("Shuffle Result 1:", result1)
        # print("Shuffle Result 2:", result2)

        if result1 != result2:
            return result1
        else:
            raise DeckCheatingError("This is not a valid deck!! Stop cheating!!")

    return wrapper


class Deck(IDeck):
    """
    A representing the standard card deck of playing cards
    """

    def __init__(self, shuffle=True):
        """
        Initialize a new deck shuffled by default.

        Args:
            shuffle: True - deck is shuffled, False - deck as is.
        """
        self._cards = Deck.build_deck()
        self._index = 0
        if shuffle:
            self.shuffle()

    @property
    def cards(self):
        """
        get the cards list of the deck

        Returns:
             cards: a list of Card objects
        """
        return self._cards

    @override
    @fair_deck
    def shuffle(self):
        """
        Shuffles the deck of cards that is the card objects list

        Returns:
             cards: a list of Card objects
        """
        # rnd.shuffle(self._cards)
        new_deck = rnd.sample(self._cards, len(self._cards))
        self._cards = new_deck
        return self._cards

    @override
    def draw(self) -> Card:
        """
        Draw the card on the top of the deck of cards removing it from the deck

        Returns:
             card: a Card object that was on the top of the deck.
        """

        return self._cards.pop() if self._cards else None

    @override
    def add_card(self, new_card: Card):
        """
        Add a card to the bottom of the deck

        Args:
            new_card: a Card object that is to be returned to the deck

        Returns:
             cards: a list of Card objects with the added Card

        """
        self._cards.append(new_card)

    @override
    def __len__(self):
        """
        Returns the amount of cards in the deck

        Returns:
            int: the number of cards currently in the deck
        """
        return len(self._cards)

    @override
    def __getitem__(self, idx):
        """
        Returns the Card at the index idx

        Args:
            idx: the index of the card wanted

        Returns:
             Card: the Card object at the index given
        """
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
        """
        a utility function to create the deck

        Returns:
             Deck: a standard card deck not shuffled
        """
        new_deck = []
        for suit in CardSuit:
            for rank in CardRank:
                card = Card(suit, rank)
                new_deck.append(card)

        return new_deck
