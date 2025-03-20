from num_array import NumberArray, NumArray
from sort_array import SortArray
from mult_array import MultiplyArray
from avg_array import AvgArray
from std_array import StdvArray
from disp_array import DisplayArray


def main():
    n_arrey = NumberArray()
    sorte = SortArray()
    multi = MultiplyArray()
    avg = AvgArray()
    stdv = StdvArray()
    disp = DisplayArray()

    print(f"\n1. if array creation is not part of the chain\n")
    head = sorte
    sorte.next = multi
    multi.next = avg
    avg.next = stdv
    stdv.next = disp

    size = int(input("Enter the size of the array: "))
    n_array = NumArray(size)
    print(f"Original array: {n_array.numbers}")
    head.handle(n_array)

    # print(f"\n2. if array creation is part of chain\n")
    # head = n_arrey
    # n_array.next = sorte
    # sorte.next = multi
    # multi.next = avg
    # avg.next = stdv
    # stdv.next = disp
    #
    # size = int(input("Enter the size of the array: "))
    # head.handle(size)


if __name__ == "__main__":
    main()
