import unittest
from powsum import powsum


class TestPowsum(unittest.TestCase):

    def test_no_arguments(self):
        self.assertEqual(powsum(), 0)

    def test_with_arguments(self):
        self.assertEqual(powsum(1, 2, 3, exp=3), 36)

    def test_default_exp(self):
        self.assertEqual(powsum(1, 2, 3), 14)

    def test_has_annotations(self):
        self.assertTrue(powsum.__annotations__)

    def test_has_docstring(self):
        self.assertTrue(powsum.__doc__)


if __name__ == '__main__':
    unittest.main()
