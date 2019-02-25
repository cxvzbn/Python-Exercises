# Define a function reverse()that computes the reversal of a string.
# For example, reverse("I am testing") should return the string "gnitset ma I"


def reverse(text):
    reversed_text = list(text)
    reversed_text.reverse()
    return "".join(reversed_text)


if __name__ == '__main__':
    msg = "Reverse of 'I am testing' is: {}".format(reverse("I am testing"))
    print(msg)
