from icard import ICard
from card_suit import CardSuit
from card_rank import CardRank
from typing import override


class Card(ICard):
    """
    A class representing the standard playing card
    """

    def __init__(self, suit: CardSuit, rank: CardRank, face_up=True):
        """
        Initialize a new card with the specified suit type and rank value, facing up by default.

        Args:
            suit: the suit of the card (clubs, spades, diamonds, hearts)
            rank: the rank of the card (2 to ace)
            face_up: is the card facing up or not
        """
        self._suit = suit
        self._rank = rank
        self._face_up = face_up

    @property
    def suit(self) -> CardSuit:
        """
        get the suit of the card

        Returns:
            CardSuit: the suit of the card
        """
        return self._suit

    @property
    def rank(self) -> CardRank:
        """
        get the rank of the card

        Returns:
            CardRank: the rank of the card
        """
        return self._rank

    @property
    def face_up(self) -> bool:
        """
        returns a bool representing weather the card is facing up or not

        Returns:
            boot: True - card facing up, False - card facing down

        """
        return self._face_up

    @override
    def flip(self) -> bool:
        """
        flips the card

        Returns:
            boot: True - card facing up, False - card facing down
        """
        self._face_up = not self._face_up
        return self._face_up

    @override
    def get_display_name(self) -> str:
        """
        returns the display name of card

        Returns:
             str: the display name of the card
        """
        if self._rank is None or self._suit is None:
            return "Invalid Card"
        return f"{self._rank} of {self._suit}"

    def __eq__(self, other):
        """
         Check if two cards are equal.

         Args:
             other: Another Card object to compare with.

         Returns:
             bool: True if the Cards have the same value and suit, False otherwise.
         """
        if not isinstance(other, Card):
            raise TypeError("Can only compare Card with another Card")
        return self._rank == other.rank and self._suit == other.suit

    def __lt__(self, other):
        """
        Check if this Card has lower value than another.

        Args:
            other: Another Card object to compare with.

        Returns:
            bool: True if this card has lower rank value than the other, if rank values are equal
             then if suit is lower, False otherwise.
        """
        if not isinstance(other, Card):
            raise TypeError("Can only compare Card with another Card")
        elif self._rank == other.rank:
            return self._suit < other.suit
        else:
            return self._rank < other.rank

    def __gt__(self, other):
        """
        Check if this Card has grater value than another.

        Args:
            other: Another Card object to compare with.

        Returns:
            bool: True if this card has grater rank value than the other, if rank values are equal
             then if suit is grater, False otherwise.
        """
        if not isinstance(other, Card):
            raise TypeError("Can only compare Card with another Card")
        elif self._rank == other.rank:
            return self._suit > other.suit
        else:
            return self._rank > other.rank

    def __hash__(self):
        """
        hash function to hash the Card

        Returns:
             hash value of Card
        """
        return hash((self._rank, self._suit))

    def __str__(self):
        """
        return card as str, if it is face up

        Returns:
         str: string representation of the card
        """
        if self._face_up:
            return self.get_display_name()
        else:
            return "?"

    def __repr__(self):
        """
        a representation of Card creation

        Returns:
             the command and parameters to create this Card
        """
        return f'Card({self._suit, self._rank, self._face_up})'
