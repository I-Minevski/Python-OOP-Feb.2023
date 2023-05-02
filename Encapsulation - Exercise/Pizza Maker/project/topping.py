class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, topping_type: str):
        if len(topping_type) != 0:
            self.__topping_type = topping_type
        else:
            raise ValueError("The topping type cannot be an empty string")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("The weight cannot be less or equal to zero")

