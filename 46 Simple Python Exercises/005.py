# Write a function translate()that will translate a text into "rövarspråket" (Swedish for "robber's
# language"). That is, double every consonant and place an occurrence of "o"in between. For example,
# translate("this is fun")should return the string "tothohisos isos fofunon".

msg1 = "Please enter a sentence: \n"


def translate(user_input):
    constans = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    new_input = list(user_input)
    for index, character in enumerate(list(user_input)):
        for constant in constans:
            if character == constant:
                new_input[index] = format(constant + "o" + constant)
    return "".join(new_input)

if __name__ == '__main__':
    print(translate(input(msg1)))
