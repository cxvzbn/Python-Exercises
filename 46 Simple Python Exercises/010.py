# Define a function overlapping()that takes two lists and returns True if they have at least one member in
# common, False otherwise. You may use your is_member()function, or the inoperator, but for the sake
# of the exercise, you should (also) write it using two nested for­loops.

msg1 = "Please enter values separated by space\n"
msg2 = "Please enter second values separated by space\n"


def overlapping(first_values, second_values):
    for first_value in first_values:
        for second_value in second_values:
            if first_value == second_value:
                return True
    return False


if __name__ == '__main__':
    print(overlapping(input(msg1).split(), input(msg2).split()))
