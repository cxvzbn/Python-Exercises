# Define a function that computes the length of a given list or string.
# (It is true that Python has the len() function built in, but writing it
# yourself is nevertheless a good exercise.)


def length(user_input):
    i = 0
    for x in user_input:
        if x != " ":
            i += 1
    return i


if __name__ == '__main__':
    random_input = "eleven"
    msg = (
        "Returns the lenght of a given list or string\n"
        "Input: {}\n"
        "Output: {}".format(random_input, length(random_input))
    )
    print(msg)
