        for i, [new_iterables] in enumerate(zip(iterables)):
            variables[i] = new_iterables
        for l in range(len(variables)):
            for j in range(len(variables[0])):
                print("xd {}".format(*variables[l]))