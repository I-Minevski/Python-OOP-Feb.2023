from project.animals.animal import Bird
from project.food import Food, Seed, Fruit, Vegetable, Meat


class Owl(Bird):
    WEIGHT_INCREASE = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food: Food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Owl.WEIGHT_INCREASE


class Hen(Bird):
    WEIGHT_INCREASE = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food: Food):
        if not isinstance(food, Food):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Hen.WEIGHT_INCREASE


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)

