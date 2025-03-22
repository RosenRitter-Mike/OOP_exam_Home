from abc import ABC, abstractmethod


class IDeck(ABC):
    """ an abstract deck class that represents the deck even if its a Coup card deck  """

    @abstractmethod
    def cards(self):
        pass

    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def add_card(self, card):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, item):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass
