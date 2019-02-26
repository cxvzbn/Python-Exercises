# Write a function char_freq() that takes a string and builds a frequency
# listing of the characters contained in it. Represent the frequency listing
# as a Python dictionary. Try it with something like
# char_freq("abbabcbdbabdbdbabababcbcbab").


def char_freq(user_input):
    list_from_string, letter_frequency = list(user_input), list()
    for letter in user_input:
        gen = [char for char in list_from_string if letter == char]
        i = 0
        for _ in gen:
            i += 1
            list_from_string.remove(letter)
        if i > 0:
            letter_frequency.append([i, letter])
    letter_frequency.sort(reverse=True)
    set(map(lambda x: print(
        "The letter \"" 
        + x[1] 
        + "\" has been counted " 
        + str(x[0]) 
        + " times."
        ), letter_frequency))


if __name__ == "__main__":
    example_input = "abbabcbdbabdbdbabababcbcbab"
    msg = (
        "Returns if a sentence is a panagram\n"
        "Input: {}\n"
        "Output:".format(example_input)
    )
    print(msg)
    char_freq("abbabcbdbabdbdbabababcbcbab")
