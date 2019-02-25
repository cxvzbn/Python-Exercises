# Define a function overlapping() that takes two lists and returns True if
# they have at least one member in common, False otherwise. You may use your
# is_member() function, or the inoperator, but for the sake of the exercise,
# you should (also) write it using two nested for ­loops.


def overlapping(first_values, second_values):
    for first_value in first_values:
        for second_value in second_values:
            if first_value == second_value:
                return True
    return False


if __name__ == '__main__':
    msg = (
        "Checks if '1532' has overlapping numbers in '4168' and '6749'\n"
        "'4168' is overlapping: {}\n"
        "'6749' is overlapping: {}".format(
        overlapping("1532", "4168"), overlapping("1532", "6749")))
    print(msg)
