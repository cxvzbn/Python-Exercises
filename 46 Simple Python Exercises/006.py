# Define a function sum()and a function multiply()that sums and multiplies (respectively) all the
# numbers in a list of numbers. For example, sum([1, 2, 3, 4])should return 10, and multiply([1,
# 2, 3, 4])should return 24.

msg1 = "Input numbers separated by space to know their sum and multiply:\n"


def sum_of_numbers(numbers_list):
    i = 0
    for number in numbers_list:
        i += number
    return i


def multiple_of_numbers(numbers_list):
    i = 1
    for number in numbers_list:
        i = i * number
    return i

if __name__ == '__main__':
    numbers = list(map(int, input(msg1).split()))
    print(sum_of_numbers(numbers))
    print(multiple_of_numbers(numbers))
