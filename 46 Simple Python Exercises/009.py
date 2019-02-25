# Write a function is_member() that takes a value (i.e. a number, string, etc)
# and a list of values a, and returns True if x is a member of a, False
# otherwise. (Note that this is exactly what the inoperator does, but for the
# sake of the exercise you should pretend Python did not have this operator).


def is_member(value, list_of_values):
    for n in list_of_values:
        if value == n:
            return True
    return False


if __name__ == '__main__':
    msg = (
        "Checks if 'a' and 'f' are members of 'abcd'\n"
        "'a' is: {}\n"
        "'f' is: {}"
        .format(is_member("a", "abcd"), is_member("f", "abcd")))
    print(msg)
