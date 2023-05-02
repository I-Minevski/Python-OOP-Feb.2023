def choose_pattern():
    pattern = input("Choose a pattern: \nTriangle\nRhomboid\nSquare\nPattern choice:")
    size = int(input("Select size:"))
    return pattern, size


def print_row(spaces, stars):
    print(' ' * spaces + '* ' * stars)


def get_pattern(*data):
    pattern, size = data

    if pattern == "Rhomboid":
        for i in range(size):
            spaces = size - i - 1
            stars = i + 1
            print_row(spaces, stars)
        for i in range(size - 2, -1, -1):
            spaces = size -i - 1
            stars = i + 1
            print_row(spaces, stars)
    elif pattern == "Triangle":
        for i in range(size):
            stars = i + 1
            print_row(0, stars)
    elif pattern == "Square":
        for i in range(size):
            print_row(0, size)


get_pattern(*choose_pattern())