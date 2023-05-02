class CustomList:
    def __init__(self):
        self.__data = []

    def append(self, value):
        self.__data.append(value)
        return self.__data

    def remove(self, index):
        return self.__data.pop(index)

    def get(self, index):
        return self.__data[index]

    def extend(self, iterable):
        self.__data.extend(iterable)
        return self.__data

    def insert(self, index, value):
        self.__data.insert(index, value)
        return self.__data

    def pop(self):
        return self.__data.pop()

    def clear(self):
        self.__data.clear()

    def index(self, value):
        return self.__data.index(value)

    def count(self, value):
        return self.__data.count(value)

    def reverse(self):
        self.__data.reverse()
        return self.__data

    def copy(self):
        new_list = CustomList()
        new_list.extend(self)
        return new_list

    def size(self):
        return len(self.__data)

    def add_first(self, value):
        self.__data.insert(0, value)

    def dictionize(self):
        dictionary = {}
        for i in range(0, len(self.__data), 2):
            if len(self.__data) % 2 != 0:
                if i == len(self.__data) - 1:
                    dictionary[self.__data[i]] = " "
                    break
            dictionary[self.__data[i]] = self.__data[i + 1]

        return dictionary

    def move(self, amount):
        self.__data = self.__data[amount:] + self.__data[:amount]
        return self.__data

    def sum(self):
        total = 0
        for value in self.__data:
            if isinstance(value, (int, float)):
                total += value
            else:
                total += len(str(value))

        return total

    def overbound(self):
        max_index = 0
        max_value = None
        for i, value in enumerate(self.__data):
            if isinstance(value, (int, float)):
                if max_value is None or value > max_value:
                    max_index = i
                    max_value = value
                else:
                    if max_value is None or len(str(value)) > max_value:
                        max_index = i
                        max_value = value

        return max_index

    def underbound(self):
        min_index = 0
        min_value = None
        for i, value in enumerate(self.__data):
            if isinstance(value, (int, float)):
                if min_value is None or value < min_value:
                    min_index = i
                    min_value = value
                else:
                    if min_value is None or len(str(value)) < min_value:
                        min_index = i
                        min_value = value

        return min_index

    def is_empty(self):
        return len(self.__data) == 0

    def remove_all_occurrences(self, value):
        self.__data = [el for el in self.__data if el != value]
        return self.__data


lst = CustomList()
lst.extend([1, 2, 3, 4, 5, 6])
print(lst.dictionize())
print(lst.move(2))