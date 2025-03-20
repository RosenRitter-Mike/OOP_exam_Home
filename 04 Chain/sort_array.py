from array_handler import ArrayHandler
from num_array import NumberArray, NumArray


class SortArray(ArrayHandler):

    def handle(self, num_array: NumArray | NumberArray) -> None:
        sort_choice = input("Sort the array? (yes/no): ").strip().lower()
        if sort_choice == "yes":
            sorted_numbers = sorted(num_array.numbers)
            num_array.numbers = sorted_numbers
            print(f"Sorted array: {num_array.numbers}")
        if self.next:
            self.next.handle(num_array)

