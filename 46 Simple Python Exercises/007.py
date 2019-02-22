# Define a function reverse()that computes the reversal of a string. For example, reverse("I am
# testing")should return the string "gnitset ma I".

msg1 = "Input a string to reverse it \n"


def reverse(text):
    reversed_text = list(text)
    reversed_text.reverse()
    return "".join(reversed_text)

if __name__ == '__main__':
    print(reverse(input(msg1)))
