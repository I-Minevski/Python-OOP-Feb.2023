from project.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):
    def setUp(self):
        self.toy_store = ToyStore()

    def test_correct_init(self):
        self.assertEqual(self.toy_store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_add_toy(self):

        self.assertEqual(self.toy_store.add_toy("A", "Barbie"), "Toy:Barbie placed successfully!")

        with self.assertRaises(Exception):
            self.toy_store.add_toy("Z", "Hot Wheels")

        self.toy_store.add_toy("B", "Lego")
        with self.assertRaises(Exception):
            self.toy_store.add_toy("B", "Teddy Bear")

        self.toy_store.add_toy("C", "Puzzle")
        with self.assertRaises(Exception):
            self.toy_store.add_toy("C", "Remote Control Car")

    def test_remove_toy(self):

        self.toy_store.add_toy("A", "Uno")
        self.toy_store.add_toy("B", "Play-Doh")

        self.assertEqual(self.toy_store.remove_toy("A", "Uno"), "Remove toy:Uno successfully!")
        self.assertIsNone(self.toy_store.toy_shelf["A"])

        with self.assertRaises(Exception):
            self.toy_store.remove_toy("B", "Uno")

        with self.assertRaises(Exception):
            self.toy_store.remove_toy("Z", "Play-Doh")
