from typing import List

from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        elif self.__budget < price:
            return "Not enough budget"
        else:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        else:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([w.salary for w in self.workers])
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending = sum([a.money_for_care for a in self.animals])
        if self.__budget >= tending:
            self.__budget -= tending
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [animal.__repr__() for animal in self.animals if isinstance(animal, Lion)]
        tigers = [animal.__repr__() for animal in self.animals if isinstance(animal, Tiger)]
        cheetahs = [animal.__repr__() for animal in self.animals if isinstance(animal, Cheetah)]
        total_animals_count = len(self.animals)
        amount_of_lions = len(lions)
        amount_of_tigers = len(tigers)
        amount_of_cheetahs = len(cheetahs)

        sep = '\n'

        return f"You have {total_animals_count} " \
               f"animals\n----- {amount_of_lions} " \
               f"Lions:\n{sep.join(lions)}" \
               f"\n----- {amount_of_tigers} " \
               f"Tigers:\n{sep.join(tigers)}" \
               f"\n----- {amount_of_cheetahs} " \
               f"Cheetahs:\n{sep.join(cheetahs)}"

    def workers_status(self):
        keepers = [worker.__repr__() for worker in self.workers if isinstance(worker, Keeper)]
        caretakers = [worker.__repr__() for worker in self.workers if isinstance(worker, Caretaker)]
        vets = [worker.__repr__() for worker in self.workers if isinstance(worker, Vet)]
        total_workers_count = len(self.workers)
        amount_of_keepers = len(keepers)
        amount_of_caretakers = len(caretakers)
        amount_of_vets = len(vets)

        sep = '\n'

        return f"You have {total_workers_count} " \
               f"workers\n----- {amount_of_keepers} " \
               f"Keepers:\n{sep.join(keepers)}" \
               f"\n----- {amount_of_caretakers} " \
               f"Caretakers:\n{sep.join(caretakers)}" \
               f"\n----- {amount_of_vets} " \
               f"Vets:\n{sep.join(vets)}"

