import sys
import unittest
import importlib
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-m', '--module', default='fpmath')
parser.add_argument('unittest_args', nargs='*')
args = parser.parse_args()

module = importlib.import_module(args.module)
isclose = module.isclose


class TestIsClose(unittest.TestCase):

    def test_no_abs_tollerance(self):
        """Return False if rel_err <= rel_tol but abs_err > abs_tol."""
        a = 0.004
        b = 0.002
        # rel_err -> 0.5, abs_err -> 0.002
        self.assertFalse(isclose(a, b, 0.6, 0.001))
        self.assertFalse(isclose(a, b, 0.5, 0.001))

    def test_no_rel_tollerance(self):
        """Return False if rel_err > rel_tol but abs_err <= abs_tol."""
        a = 0.004
        b = 0.002
        # rel_err -> 0.5, abs_err -> 0.002
        self.assertFalse(isclose(a, b, 0.4, 0.003))
        self.assertFalse(isclose(a, b, 0.4, 0.002))

    def test_no_rel_and_no_abs_tollerances(self):
        """Return False if rel_err > rel_tol and abs_err > abs_tol."""
        a = 0.004
        b = 0.002
        # rel_err -> 0.5, abs_err -> 0.002
        self.assertFalse(isclose(a, b, 0.4, 0.001))

    def test_ok_rel_and_abs_tollerances(self):
        """Return True if rel_err <= rel_tol and abs_err <= abs_tol."""
        a = 0.004
        b = 0.002
        # rel_err -> 0.5, abs_err -> 0.002
        self.assertTrue(isclose(a, b, 0.6, 0.003))
        self.assertTrue(isclose(a, b, 0.5, 0.002))

    def test_ok_negative_numbers(self):
        """Negative floats, rel_err <= rel_tol and abs_err <= abs_tol."""
        a = -0.004
        b = -0.002
        # rel_err -> 0.5, abs_err -> 0.002
        self.assertTrue(isclose(a, b, 0.6, 0.003))
        self.assertTrue(isclose(a, b, 0.5, 0.002))

    def test_negative_rel_tol(self):
        with self.assertRaises(ValueError):
            isclose(1, 2, -1, 1)

    def test_negative_abs_tol(self):
        with self.assertRaises(ValueError):
            isclose(1, 2, 1, -1)


if __name__ == '__main__':
    sys.argv[1:] = args.unittest_args
    unittest.main()
