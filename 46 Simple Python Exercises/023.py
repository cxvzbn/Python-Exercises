# Define a simple "spelling correction" function correct() that takes a string
# and sees to it that 1) two or more occurrences of the space character is
# compressed into one, and 2) inserts an extra space after a period if the
# period is directly followed by a letter. E.g. correct ("This is very funny
# and cool.Indeed!") should return "This is very funny and cool. Indeed!"
# Tip: Use regular expressions!


def correct(sentence):
    new_sentence = ""
    for i in range(0, len(sentence)):
        if i < len(sentence):
            if sentence[i] == " " and sentence[i+1] == " ":
                new_sentence += ""
            elif sentence[i] == "." and sentence[i+1] != " ":
                new_sentence += ". "
            else:
                new_sentence += sentence[i]
    return new_sentence


if __name__ == "__main__":
    example_input = "This  is very  funny and   cool.Indeed!"
    msg = (
        "Returns spelling correction defined in the exercise\n"
        "Input: {}\n"
        "Output: {}\n".format(example_input, correct(example_input))
    )
    print(msg)
