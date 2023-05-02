def print_row(spaces, stars):
    print(' ' * spaces + '* ' * stars)


size = int(input())
for i in range(size):
    spaces = size - i - 1
    stars = i + 1
    print_row(spaces, stars)
for i in range(size - 2, -1, -1):
    spaces = size - i - 1
    stars = i + 1
    print_row(spaces, stars)