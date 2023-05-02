from project.product import Product
from project.food import Food
from project.drink import Drink


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> [Product, None]:
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join(f"{product.name}: {product.quantity}" for product in self.products)




