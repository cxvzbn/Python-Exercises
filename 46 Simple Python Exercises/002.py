# Define a function max_of_three()that takes three numbers as arguments and returns the largest of
# them

msg = "Prosze podac liczby oddzielone spacja: \n"


def max_of_any(numbers):
    int_typed = [int(x) for x in numbers]
    int_typed.sort(reverse=True)
    return int_typed[0]


if __name__ == '__main__':
    print(max_of_any(input(msg).split()))
