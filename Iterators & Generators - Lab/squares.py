def squares(n):
    for i in range(1, n + 1):
        yield i * i


#squares1 = (x * x for x in [1, 2, 3, 4 ,5])

print(list(squares(5)))
