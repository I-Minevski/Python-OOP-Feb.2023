from project.animals.animal import Mammal
from project.food import Food, Seed, Fruit, Vegetable, Meat


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.10

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food: Food):
        if not isinstance(food, (Vegetable, Fruit)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Mouse.WEIGHT_INCREASE


class Dog(Mammal):
    WEIGHT_INCREASE = 0.40

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Dog.WEIGHT_INCREASE


class Cat(Mammal):
    WEIGHT_INCREASE = 0.30

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food: Food):
        if not isinstance(food, (Vegetable, Meat)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Cat.WEIGHT_INCREASE


class Tiger(Mammal):
    WEIGHT_INCREASE = 1

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Tiger.WEIGHT_INCREASE


