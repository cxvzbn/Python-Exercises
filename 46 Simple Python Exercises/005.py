# Write a function translate()that will translate a text into "rövarspråket"
# (Swedish for "robber's language"). That is, double every consonant and place
# an occurrence of "o"in between. For example, translate("this is fun") should 
# return the string "tothohisos isos fofunon".

msg1 = "Please enter a sentence: \n"


def translate(user_input):
    constans = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    new_input = list(user_input)
    for index, character in enumerate(user_input):
        for constant in constans:
            if character == constant:
                new_input[index] = "{}o{}".format(constant, constant)
    return "".join(new_input)


if __name__ == '__main__':
    random_input = "this is fun"
    msg = (
        "Returns the Robber's language from a string\n"
        "Input: {}\n"
        "Output: {}".format(random_input, translate(random_input))
    )
    print(msg)