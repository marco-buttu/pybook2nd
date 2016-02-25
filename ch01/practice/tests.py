import unittest
from unique import unique
from onlyone import onlyone, onlyone2
from square import Square


class TestUnique(unittest.TestCase):

    def test_unique(self):
        self.assertEqual(unique('programmare'), 4)


class TestOnlyOne(unittest.TestCase):

    def test_onlyone(self):
        self.assertEqual(onlyone('programmare'), 7)
        self.assertEqual(onlyone2('programmare'), 7)


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.square = Square(5)

    def test_perimeter(self):
        self.assertEqual(self.square.perimeter(), 20)

    def test_area(self):
        self.assertEqual(self.square.area(), 25)


if __name__ == '__main__':
    unittest.main()
