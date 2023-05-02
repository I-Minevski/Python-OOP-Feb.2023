from itertools import permutations


def possible_permutations(sequence):
    # for el in list(permutations(sequence)):
    #  yield list(el)

    if len(sequence) == 0:
        yield []
    elif len(sequence) == 1:
        yield sequence
    else:
        for i in range(len(sequence)):
            rest = sequence[:i] + sequence[i + 1:]
            for perm in possible_permutations(rest):
                yield [sequence[i]] + perm


[print(n) for n in possible_permutations([1, 2, 3, 4])]
