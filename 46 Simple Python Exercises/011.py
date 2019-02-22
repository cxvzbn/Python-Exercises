# Define a function generate_n_chars()that takes an integer nand a character cand returns a string, n
# characters long, consisting only of c:s. For example, generate_n_chars(5,"x")should return the
# string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x"that will evaluate
# to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner.)

msg1 = "Enter the number of times that you want to repeat the character:\n"
msg2 = "Enter the character that you want to repeat:\n"


def generate_n_chars(n, c):
    k = list(c)
    for _ in range(1, n):
        k.append(c)
    return "".join(k)

if __name__ == '__main__':
    print(generate_n_chars(int(input(msg1)), input(msg2)))
