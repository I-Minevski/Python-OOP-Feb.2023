from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def available_processors(self):
        ...

    @property
    @abstractmethod
    def available_ram(self):
        ...

    @property
    @abstractmethod
    def computer_type(self):
        ...

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")

        if ram not in self.available_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.computer_type} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.available_processors[processor] + self.ram_price(ram)
        return f"Created {self} for {self.price}$."

    def ram_price(self, ram):
        return (self.available_ram.index(ram) + 1) * 100

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"