# Alejandra Castillo 1440370
# Descending selection sort with output during execution
# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order
def selection_sort_descend_trace(numbers):
    # defined the sorting
    for a in range(len(numbers) - 1):
        ind = a
        for b in range(a + 1, len(numbers)):
            if numbers[b] > numbers[ind]:
                ind = b
        numbers[a], numbers[ind] = numbers[ind], numbers[a]
        for x in numbers:
            print(x, end='')
            print()


if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    # number splitting
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)
