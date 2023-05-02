from project.mammal import Mammal
import unittest


class MammalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Rex", "Canine", "Bark")

    def test_init(self):
        self.assertEqual(self.mammal.name, "Rex")
        self.assertEqual(self.mammal.type, "Canine")
        self.assertEqual(self.mammal.sound, "Bark")
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual(result, "Rex makes Bark")

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual(result, "animals")

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual(result, "Rex is of type Canine")


if __name__ == "__main__":
    unittest.main()