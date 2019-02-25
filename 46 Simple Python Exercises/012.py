# Define a procedure histogram() that takes a list of integers and prints
# a histogram to the screen. For example, histogram([4, 9, 7]) should print
# the following:
# ****
# *********
# *******


def histogram(user_input):
    for n in user_input:
        print("*" * int(n))


if __name__ == '__main__':
    print("Making a histogram out of [4, 9, 7]:")
    histogram([4, 9, 7])
