class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, flour_type: str):
        if len(flour_type) != 0:
            self.__flour_type = flour_type
        else:
            raise ValueError("The flour type cannot be an empty string")

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, baking_technique: str):
        if len(baking_technique) != 0:
            self.__baking_technique = baking_technique
        else:
            raise ValueError("The baking technique cannot be an empty string")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("The weight cannot be less or equal to zero")