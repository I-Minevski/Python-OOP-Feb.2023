from extended_list import IntegerList
import unittest


class IntegerListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.int_list = IntegerList(1, 2, 3, 4, 5)

    def test_add_valid_integer(self):
        self.int_list.add(6)
        self.assertListEqual(self.int_list.get_data(), [1, 2, 3, 4, 5, 6])

    def test_add_invalid_element(self):
        with self.assertRaises(ValueError) as context:
            self.int_list.add('a')
        self.assertEqual(str(context.exception), 'Element is not Integer')

    def test_remove_index_valid_index(self):
        self.assertEqual(self.int_list.remove_index(2), 3)
        self.assertListEqual(self.int_list.get_data(), [1, 2, 4, 5])

    def test_remove_index_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.int_list.remove_index(5)
        self.assertEqual(str(context.exception), 'Index is out of range')

    def test_get_valid_index(self):
        self.assertEqual(self.int_list.get(2), 3)

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.int_list.get(5)
        self.assertEqual(str(context.exception), 'Index is out of range')

    def test_insert_valid_index_and_element(self):
        self.int_list.insert(2, 7)
        self.assertListEqual(self.int_list.get_data(), [1, 2, 7, 3, 4, 5])

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError):
            self.int_list.insert(6, 7)

    def test_insert_invalid_element(self):
        with self.assertRaises(ValueError):
            self.int_list.insert(2, 'a')

    def test_get_biggest(self):
        self.assertEqual(self.int_list.get_biggest(), 5)

    def test_get_index_valid_element(self):
        self.assertEqual(self.int_list.get_index(3), 2)

    def test_get_index_invalid_element(self):
        with self.assertRaises(ValueError):
            self.int_list.get_index(6)


if __name__ == '__main__':
    unittest.main()