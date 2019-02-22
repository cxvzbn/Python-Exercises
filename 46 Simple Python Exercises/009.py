# Write a function is_member()that takes a value (i.e. a number, string, etc) xand a list of values a, and
# returns Trueif xis a member of a, Falseotherwise. (Note that this is exactly what the inoperator does,
# but for the sake of the exercise you should pretend Python did not have this operator.)

msg1 = "Please enter a value to check if it's a member of a list\n"
msg2 = "Please enter values separated by space\n"


def is_member(value, list_of_values):
    for n in list_of_values:
        if value == n:
            return True
    return False

if __name__ == '__main__':
    print(is_member(input(msg1), input(msg2).split()))
