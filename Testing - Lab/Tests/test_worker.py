from worker import Worker
import unittest


class WorkerTests(unittest.TestCase):

    def setUp(self):
        self.test_worker = Worker("John Smith", 10000, 10)

    def test_init_attributes(self):
        self.assertEqual(self.test_worker.name, "John Smith")
        self.assertEqual(self.test_worker.salary, 10000)
        self.assertEqual(self.test_worker.energy, 10)

    def test_rest(self):
        self.test_worker.rest()
        self.assertEqual(self.test_worker.energy, 11)

    def test_work_with_zero_energy_error(self):
        self.test_worker.energy = 0
        with self.assertRaises(Exception) as context:
            self.test_worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_work_with_negative_energy_error(self):
        self.test_worker.energy = -1
        with self.assertRaises(Exception) as context:
            self.test_worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_work_method(self):
        self.test_worker.work()
        self.assertEqual(self.test_worker.energy, 9)
        self.assertEqual(self.test_worker.money, 10000)

    def test_get_info(self):
        result = self.test_worker.get_info()
        self.assertEqual(result, "John Smith has saved 0 money.")

        self.test_worker.work()
        result = self.test_worker.get_info()
        self.assertEqual(result, "John Smith has saved 10000 money.")


if __name__ == '__main__':
    unittest.main()
