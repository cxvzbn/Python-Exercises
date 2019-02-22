# Define a procedure histogram()that takes a list of integers and prints a histogram to the screen. For
# example, histogram([4, 9, 7])should print the following:
# ****
# *********
# *******

msg1 = "Please input integers separated by space for a histogram:\n"


def histogram(user_input):
    for n in user_input.split():
        print("*" * int(n))

if __name__ == '__main__':
        histogram(input(msg1))
