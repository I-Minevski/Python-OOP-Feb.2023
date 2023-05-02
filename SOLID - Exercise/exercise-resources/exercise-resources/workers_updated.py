from abc import ABCMeta, abstractmethod, ABC
import time


class Workable(ABC):
    def work(self):
        ...


class Eatable(ABC):
    def eat(self):
        ...


class Worker(Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        ...


class WorkManager(Manager):

    def set_worker(self, worker):
        assert isinstance(worker, Workable), "`worker` must be of type {}".format(Workable)

        self.worker = worker

    def manage(self):
        self.worker.work()


class LunchManager(Manager):

    def set_worker(self, worker):
        assert isinstance(worker, Eatable), "`worker` must be of type {}".format(Eatable)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


class Robot(Workable):

    def work(self):
        print("I'm a robot. I'm working....")


work_manager = WorkManager()
work_manager.set_worker(Worker())
work_manager.manage()

lunch_manager = LunchManager()
lunch_manager.set_worker(Worker())
lunch_manager.lunch_break()

work_manager.set_worker(SuperWorker())
work_manager.manage()

lunch_manager.set_worker(SuperWorker())
lunch_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()


