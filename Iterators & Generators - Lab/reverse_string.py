def reverse_text(string):
    index = len(string)
    while index > 0:
        index -= 1
        yield string[index]


for char in reverse_text("step"):
    print(char, end='')
