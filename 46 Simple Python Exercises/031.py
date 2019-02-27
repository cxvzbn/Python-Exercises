# Implement the higher order functions map(), filter()and reduce().
# (They are built­in but writing them yourself may be a good exercise.)


def new_map(function, *iterables):
    output = list()
    for j in range(len(iterables[0])):
        temp = list()
        for k in range(len(iterables)):
            temp.append(iterables[k][j])
        output.append(function(*temp))
    return output


if __name__ == "__main__":
    output = new_map(lambda x, y, z: x*y*z, [2, 7, 4], [6, 2, 1], [7, 4, 9])
    print(output)
