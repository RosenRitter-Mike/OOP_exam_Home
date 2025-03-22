from abc import ABC, abstractmethod


class ICard(ABC):
    """ an abstract card class that represents the card, so if a tarot, taki or other kind of card  """

    @abstractmethod
    def suit(self):
        pass

    @abstractmethod
    def rank(self):
        pass

    @abstractmethod
    def face_up(self):
        pass

    @abstractmethod
    def flip(self) -> bool:
        pass

    @abstractmethod
    def get_display_name(self) -> str:
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


