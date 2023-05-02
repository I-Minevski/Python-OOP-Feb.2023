from project.truck_driver import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):
    def setUp(self):
        self.truck_driver = TruckDriver("John", 1.40)

    def test_init(self):
        self.assertEqual(self.truck_driver.name, "John")
        self.assertEqual(self.truck_driver.money_per_mile, 1.40)
        self.assertEqual(self.truck_driver.available_cargos, {})
        self.assertEqual(self.truck_driver.earned_money, 0)
        self.assertEqual(self.truck_driver.miles, 0)

    def test_earned_money_error(self):
        with self.assertRaises(ValueError) as context:
            self.truck_driver.earned_money = -5
        self.assertEqual(str(context.exception), f"{self.truck_driver.name} went bankrupt.")

    def test_add_cargo_offer(self):
        self.assertEqual(self.truck_driver.add_cargo_offer("New York", 500),
                         "Cargo for 500 to New York was added as an offer.")

        self.assertEqual(self.truck_driver.available_cargos["New York"], 500)

    def test_add_cargo_offer_exception(self):
        self.truck_driver.add_cargo_offer("New York", 500)
        with self.assertRaises(Exception) as context:
            self.truck_driver.add_cargo_offer("New York", 500)
        self.assertEqual(str(context.exception), "Cargo offer is already added.")

    def test_drive_best_cargo_offer(self):
        self.truck_driver.add_cargo_offer("Texas", 2000)
        self.truck_driver.add_cargo_offer("Washington", 20000)

        result = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual(result, f"{self.truck_driver.name} is driving 20000 to Washington.")
        self.assertEqual(self.truck_driver.earned_money, 4000)
        self.assertEqual(self.truck_driver.miles, 20000)

    def test_drive_best_cargo_offer_error(self):
        self.assertEqual(self.truck_driver.drive_best_cargo_offer(), "There are no offers available.")

    def test_eat(self):
        self.truck_driver.earned_money = 100

        self.truck_driver.eat(250)
        self.truck_driver.eat(500)

        self.assertEqual(self.truck_driver.earned_money, 60)

    def test_sleep(self):
        self.truck_driver.earned_money = 100

        self.truck_driver.sleep(1000)
        self.truck_driver.sleep(2000)

        self.assertEqual(self.truck_driver.earned_money, 10)

    def test_pump_gas(self):
        self.truck_driver.earned_money = 2000

        self.truck_driver.pump_gas(1500)
        self.truck_driver.pump_gas(3000)

        self.assertEqual(self.truck_driver.earned_money, 1000)

    def repair_truck(self):
        self.truck_driver.earned_money = 16000

        self.truck_driver.repair_truck(10000)
        self.truck_driver.repair_truck(20000)

        self.assertEqual(self.truck_driver.earned_money, 1000)

    def test_repr(self):
        self.truck_driver.miles = 1000
        self.assertEqual(repr(self.truck_driver), "John has 1000 miles behind his back.")


