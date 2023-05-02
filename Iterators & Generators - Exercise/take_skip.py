class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.number = 0 - self.step

    def __iter__(self):
        return self

    def __next__(self):
        while self.count > 0:
            self.number += self.step
            self.count -= 1
            return self.number
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
