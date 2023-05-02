from car_manager import Car
import unittest


class CarManagerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('Audi', 'RS5', 10, 60)

    def test_init(self):
        self.assertEqual(self.car.make, 'Audi')
        self.assertEqual(self.car.model, 'RS5')
        self.assertEqual(self.car.fuel_consumption, 10)
        self.assertEqual(self.car.fuel_capacity, 60)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_validation(self):
        with self.assertRaises(Exception) as context:
            Car("", "Mustang", 10, 50)
        self.assertEqual(str(context.exception), 'Make cannot be null or empty!')

    def test_model_validation(self):
        with self.assertRaises(Exception) as context:
            Car("Ford", "", 10, 50)
        self.assertEqual(str(context.exception), 'Model cannot be null or empty!')

    def test_fuel_consumption_validation(self):
        with self.assertRaises(Exception) as context:
            Car("Ford", "Mustang", -10, 50)
        self.assertEqual(str(context.exception), 'Fuel consumption cannot be zero or negative!')

    def test_fuel_capacity_validation(self):
        with self.assertRaises(Exception) as context:
            Car("Ford", "Mustang", 10, -50)
        self.assertEqual(str(context.exception), 'Fuel capacity cannot be zero or negative!')

    def test_fuel_amount_validation(self):
        with self.assertRaises(Exception) as context:
            car = Car("Ford", "Mustang", 10, 50)
            car.fuel_amount = -10
        self.assertEqual(str(context.exception), 'Fuel amount cannot be negative!')

    def test_refuel_error(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-5)
        self.assertEqual(str(context.exception), 'Fuel amount cannot be zero or negative!')

    def test_refuel(self):
        self.car.refuel(20)
        self.assertEqual(self.car.fuel_amount, 20)

    def test_refuel_at_full_capacity(self):
        self.car.refuel(60)
        self.assertEqual(self.car.fuel_amount, 60)

    def test_drive_error(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(1000)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")

    def test_drive(self):
        self.car.refuel(50)
        self.car.drive(200)
        self.assertEqual(self.car.fuel_amount, 30)


if __name__ == '__main__':
    unittest.main()