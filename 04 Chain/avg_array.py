from array_handler import ArrayHandler
from num_array import NumberArray, NumArray
import numpy as np


class AvgArray(ArrayHandler):

    def handle(self, num_array: NumArray | NumberArray) -> None:
        average_choice = input("Calculate average? (yes/no): ").strip().lower()
        if average_choice == "yes":
            calculated_average = np.mean(num_array.numbers)
            num_array.average = calculated_average
            print(f"Average of numbers: {num_array.average}")
        if self.next:
            self.next.handle(num_array)
