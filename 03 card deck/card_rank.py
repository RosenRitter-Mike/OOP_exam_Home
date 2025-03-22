from enum import Enum


class CardRank(Enum):
    """
      Enum representing different ranks of cards with their corresponding values.

    """
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __eq__(self, other):
        """
        Check if two card ranks are equal.

        Args:
            other: Another CardRank type object to compare with.

        Returns:
            bool: True if the CardRank types have the same value, False otherwise.
        """
        if not isinstance(other, CardRank):
            return False
        return self.value == other.value

    def __lt__(self, other):
        """
        Check if this CardRank type has lower value than another.

        Args:
            other: Another CardRank object to compare with.

        Returns:
            bool: True if this card has lower rank value than the other, False otherwise.
        """
        if not isinstance(other, CardRank):
            raise TypeError("Can only compare CardRank with another CardRank")
        return self.value < other.value

    def __gt__(self, other):
        """
        Check if this CardRank type has higher value than another.

        Args:
            other: Another CardRank object to compare with.

        Returns:
            bool: True if this card has higher rank value than the other, False otherwise.
        """
        if not isinstance(other, CardRank):
            raise TypeError("Can only compare CardRank with another CardRank")
        return self.value > other.value

    def __str__(self) -> str:
        """
        return card suit as str

        Returns:
         str: string representation of card suit
        """
        match self:
            case CardRank.JACK:
                return "Jack"
            case CardRank.QUEEN:
                return "Queen"
            case CardRank.KING:
                return "King"
            case CardRank.ACE:
                return "Ace"
            case _:
                return str(self.value)
