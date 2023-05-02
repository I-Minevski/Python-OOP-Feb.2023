    from typing import List
from project.dvd import DVD
from project.customer import Customer


class MovieWorld:
    CUSTOMER_CAPACITY = 10
    DVD_CAPACITY = 15

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = next((c for c in self.customers if c.id == customer_id), None)
        dvd = next((d for d in self.dvds if d.id == dvd_id), None)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        elif dvd.is_rented:
            return "DVD is already rented"

        elif dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        else:
            customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = next((c for c in self.customers if c.id == customer_id), None)
        dvd = next((d for d in self.dvds if d.id == dvd_id), None)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        result += '\n'.join(cust.__repr__() for cust in self.customers)
        result += '\n'
        result += '\n'.join(dvd.__repr__() for dvd in self.dvds)
        return result


