from array_handler import ArrayHandler
from num_array import NumberArray, NumArray
import statistics


class StdvArray(ArrayHandler):

    def handle(self, num_array: NumArray | NumberArray) -> None:
        std_choice = input("Calculate standard deviation? (yes/no): ").strip().lower()
        if std_choice == "yes":
            if len(num_array.numbers) > 1:
                calculated_std = statistics.stdev(num_array.numbers)
                num_array.std_deviation = calculated_std
                print(f"Standard deviation: {num_array.std_deviation}")
            else:
                print("Cannot calculate standard deviation with less than 2 numbers")
        if self.next:
            self.next.handle(num_array)
