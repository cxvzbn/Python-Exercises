# Define a function max_of_three()that takes three numbers as arguments and returns the largest of
# them

msg = "Highest number from input\nInput: 1 3 4 6 2"


def max_of_any(numbers):
    int_typed = [int(x) for x in numbers.split()]
    int_typed.sort(reverse=True)
    return int_typed[0]


if __name__ == '__main__':
    print(msg)
    print("Output: " + str(max_of_any("1 3 4 6 2")))
