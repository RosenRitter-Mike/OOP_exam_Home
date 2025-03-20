from array_handler import ArrayHandler
import random


class NumArray:
    def __init__(self, size):
        # Initialize array with random numbers
        self._numbers = [random.randint(1, 100) for _ in range(size)]
        self._average = None
        self._std_deviation = None

        # Getters

    @property
    def numbers(self):
        return self._numbers

    @property
    def average(self):
        return self._average

    @property
    def std_deviation(self):
        return self._std_deviation

    # Setters
    @numbers.setter
    def numbers(self, new_numbers):
        self._numbers = new_numbers

    @average.setter
    def average(self, value):
        self._average = value

    @std_deviation.setter
    def std_deviation(self, value):
        self._std_deviation = value


class NumberArray(ArrayHandler):
    def __init__(self):
        super().__init__()
        self._numbers = []
        self._average = None
        self._std_deviation = None

        # Getters

    @property
    def numbers(self):
        return self._numbers

    @property
    def average(self):
        return self._average

    @property
    def std_deviation(self):
        return self._std_deviation

    # Setters
    @numbers.setter
    def numbers(self, new_numbers):
        self._numbers = new_numbers

    @average.setter
    def average(self, value):
        self._average = value

    @std_deviation.setter
    def std_deviation(self, value):
        self._std_deviation = value

    def handle(self, size) -> None:
        # Initialize array with random numbers
        self._numbers = [random.randint(1, 100) for _ in range(size)]
        print(f"Original array: {self._numbers}")
        if hasattr(self, "next") and self.next:
            self.next.handle(self)
