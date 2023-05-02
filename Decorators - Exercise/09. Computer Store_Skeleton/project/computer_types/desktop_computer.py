from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    @property
    def available_processors(self):
        return {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }

    @property
    def available_ram(self):
        return [2 ** x for x in range(1, 8)]

    @property
    def computer_type(self):
        return "desktop computer"
