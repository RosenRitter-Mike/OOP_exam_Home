from array_handler import ArrayHandler
from num_array import NumberArray, NumArray


class MultiplyArray(ArrayHandler):

    def handle(self, num_array: NumArray | NumberArray) -> None:
        multiply_choice = input("Multiply array elements by a number? (yes/no): ").strip().lower()
        if multiply_choice == "yes":
            factor = int(input("Enter the multiplication factor: "))
            multiplied_numbers = [num * factor for num in num_array.numbers]
            num_array.numbers = multiplied_numbers
            print(f"Array after multiplication: {num_array.numbers}")
        if self.next:
            self.next.handle(num_array)
