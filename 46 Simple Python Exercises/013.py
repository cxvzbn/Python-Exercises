# The function max() from exercise 1) and the function max_of_three() from
# exercise 2) will only work for two and three numbers, respectively.
# But suppose we have a much larger number of numbers, or suppose we cannot
# tell in advance how many they are? Write a function max_in_list() that takes
# a list of numbers and returns the largest one.


# SAME AS FROM EXERCISE 2

def max_of_any(numbers):
    numbers.sort(reverse=True)
    return numbers[0]


if __name__ == '__main__':
    example_input = [5, 236, 7, 12, 124, 235, 1, 222]
    liczby = [int(x) for x in example_input]
    msg = (
        "Returns the largest number\n"
        "Input: {}\n"
        "Output: {}".format(example_input, max_of_any(liczby))
    )
    print(msg)
