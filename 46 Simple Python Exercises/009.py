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
    random_input = ["abcd", "a", "f"]
    msg = (
        "Returns if a value is a member of an another value\n"
        "Input: {input}\n"
        "Output: \n"
        "{input_1} is: {output_1}\n"
        "{input_2} is: {output_2}".format(
            input=random_input,
            input_1=random_input[1],
            input_2=random_input[2],
            output_1=is_member(random_input[0], random_input[1]),
            output_2=is_member(random_input[0], random_input[2])
        )
    )
    print(msg)
