from project.vehicle import Vehicle
import unittest


class VehicleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(50, 300)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 50)
        self.assertEqual(self.vehicle.horse_power, 300)
        self.assertEqual(self.vehicle.capacity, 50)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive_correct_fuel_reduction(self):
        self.vehicle.drive(4)
        self.assertEqual(self.vehicle.fuel, 45)

    def test_drive_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(10000)
        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_refuel_correct_fuel_addition(self):
        self.vehicle.drive(20)
        self.vehicle.refuel(10)
        self.assertEqual(self.vehicle.fuel, 35)

    def test_refuel_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(100)
        self.assertEqual(str(context.exception), "Too much fuel")

    def test_str(self):
        self.assertEqual(str(self.vehicle), f"The vehicle has 300 horse power with "
                                            f"50 fuel left and 1.25 fuel consumption")


if __name__ == "__main__":
    unittest.main()