from array_handler import ArrayHandler
from num_array import NumberArray, NumArray


class DisplayArray(ArrayHandler):

    def handle(self, num_array: NumArray | NumberArray) -> None:
        print(f"Final array: {num_array.numbers}")
        multiply_choice = input("Print stored statistics? (yes/no): ").strip().lower()
        if multiply_choice == "yes":
            print("\nStored Statistics:")
            if num_array.average is not None:
                print(f"Average: {num_array.average:.3f}")
            if num_array.std_deviation is not None:
                print(f"Standard Deviation: {num_array.std_deviation:.3f}")
        if self.next:
            self.next.handle(num_array)



