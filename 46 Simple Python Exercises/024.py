# The third person singular verb form in English is distinguished by the
# suffixe­s, which is added to the stem of the infinitive form: run ­> runs.
# A simple set of rules can be given as follows: 
#
# 1. If the verb ends in y, remove it and add ies 
# 2. If the verb ends in o, ch, s, sh, x or z, add es
# 3. By default just add s
#
# Your task in this exercise is to define a function make_3sg_form() which
# given a verb in infinitive form returns its third person singular form.
# Test your function with words like try, brush, run and fix. Note however
# that the rules must be regarded as heuristic, in the sense that you must not
# expect them to work for all cases. Tip: Check out the string method
# endswith().


def make_3sg_form(verb):
    suffixes = ["ch", "sh", "o", "s",  "x", "z"]
    for suffix in suffixes:
        if verb.endswith("y"):
            return "{0}ies".format(verb[:-1])
        elif verb.endswith(suffix):
            return "{0}es".format(verb)
    return verb + "s"


if __name__ == "__main__":

    example_input = ["try", "brush", "run", "fix"]
    msg = (
        "Returns its third person singular form\n"
        "Input: {}\n"
        "Output:".format(example_input)
    )
    print(msg)
    for verb in example_input:
        print("'{}' - '{}'".format(verb, make_3sg_form(verb)))
