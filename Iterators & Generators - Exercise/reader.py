def read_next(*args):
    for arg in args:
        for element in arg:
            yield element


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
