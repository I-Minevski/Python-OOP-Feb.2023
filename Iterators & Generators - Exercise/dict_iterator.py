class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.dictionary.keys()):
            key = list(self.dictionary.keys())[self.index]
            value = self.dictionary[key]
            self.index += 1
            return (key, value)
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
