from project.computer_types.computer import Computer


class Laptop(Computer):
    @property
    def available_processors(self):
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }

    @property
    def available_ram(self):
        return [2 ** x for x in range(1, 7)]

    @property
    def computer_type(self):
        return "laptop"

