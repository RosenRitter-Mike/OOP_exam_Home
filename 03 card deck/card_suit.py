from enum import Enum


class CardSuit(Enum):
    """
      Enum representing different types of card suits with their corresponding simbols.
      And the logic: SPADES > HEARTS > DIAMONDS > CLUBS
    """
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __eq__(self, other):
        """
        Check if two card suits are equal.

        Args:
            other: Another CardSuit type object to compare with.

        Returns:
            bool: True if the cards have the same suit, False otherwise.
        """
        if not isinstance(other, CardSuit):
            return False
        return self.value == other.value

    def __lt__(self, other):
        """
        Check if this CardSuit type has lower value than another.

        Args:
            other: Another CardSuit object to compare with.

        Returns:
            bool: True if this card has lower suit value than the other, False otherwise.
        """
        if not isinstance(other, CardSuit):
            raise TypeError("Can only compare CardSuit with another CardSuit")
        return self.value < other.value

    def __gt__(self, other):
        """
        Check if this CardSuit type has higher value than another.

        Args:
            other: Another CardSuit object to compare with.

        Returns:
            bool: True if this card has higher suit value than the other, False otherwise.
        """
        if not isinstance(other, CardSuit):
            raise TypeError("Can only compare CardSuit with another CardSuit")
        return self.value > other.value

    def __str__(self) -> str:
        """
        return card suit as str

        Returns:
         str: string representation of card suit
        """
        match self:
            case CardSuit.CLUBS:
                return "Clubs"
            case CardSuit.DIAMONDS:
                return "Diamonds"
            case CardSuit.HEARTS:
                return "Hearts"
            case CardSuit.SPADES:
                return "Spades"
