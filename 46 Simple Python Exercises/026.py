# Using the higher order function reduce(), write a function max_in_list()that takes a list of numbers
# and returns the largest one. Then ask yourself: why define and call a new function, when I can just as well
# call the reduce()function directly?
from functools import reduce

# 1)


def max_in_list(numbers):
    return reduce(max, numbers)


if __name__ == "__main__":

    # 1)
    print(max_in_list([1, 2, 3, 6, 5]))

    # 2)
    print(reduce(max, [1, 2, 3, 4, 5, 6, 23, 2, 677, 234]))
