# Define a function is_palindrome()that recognizes palindromes
# (i.e. words that look the same written backwards). For example,
# is_palindrome("radar") should return True.


def is_palindrome(word):
    word_list = list(word)
    word_list_reversed = word_list.copy()
    word_list_reversed.reverse()
    if "".join(word_list) == "".join(word_list_reversed):
        return True
    return False


if __name__ == '__main__':
    random_input = ["radar", "not a palindrome"]
    msg = (
        "Returns if a word is a palindrome\n"
        "Input: {input}\n"
        "Output: \n"
        "{input_1} is: {output_1}\n"
        "{input_2} is: {output_2}".format(
            input=random_input,
            input_1=random_input[0],
            input_2=random_input[1],
            output_1=is_palindrome(random_input[0]),
            output_2=is_palindrome(random_input[1])
        )
    )
    print(msg)
