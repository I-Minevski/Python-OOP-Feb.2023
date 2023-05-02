def fibonacci():
    current = 0
    following = 1
    while True:
        yield current
        yield following
        current += following
        following += current


generator = fibonacci()
for i in range(16):
    print(next(generator))

