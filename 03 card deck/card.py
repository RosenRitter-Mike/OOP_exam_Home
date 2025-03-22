from icard import ICard
from card_suit import CardSuit
from card_rank import CardRank
from typing import override


class Card(ICard):
    """
    A class representing the standard playing card
    """

    def __init__(self, suit: CardSuit, rank: CardRank, face_up=True):
        self._suit = suit
        self._rank = rank
        self._face_up = face_up

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    @property
    def face_up(self):
        return self._face_up

    @override
    def flip(self) -> bool:
        self._face_up = not self._face_up
        return self._face_up

    @override
    def get_display_name(self) -> str:
        if self._rank is None or self._suit is None:
            return "Invalid Card"
        return f"{self._rank} of {self._suit}"

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise TypeError("Can only compare Card with another Card")
        return self._rank == other.rank and self._suit == other.suit

    def __lt__(self, other):
        if not isinstance(other, Card):
            raise TypeError("Can only compare Card with another Card")
        elif self._rank == other.rank:
            return self._suit < other.suit
        else:
            return self._rank < other.rank

    def __gt__(self, other):
        if not isinstance(other, Card):
            raise TypeError("Can only compare Card with another Card")
        elif self._rank == other.rank:
            return self._suit > other.suit
        else:
            return self._rank > other.rank

    def __hash__(self):
        return hash((self._rank, self._suit))

    def __str__(self):
        if self._face_up:
            return self.get_display_name()
        else:
            return "?"

    def __repr__(self):
        return f'Card({self._suit, self._rank, self._face_up})'
