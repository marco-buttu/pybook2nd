import unittest
from reverse import reverse


class TestReverse(unittest.TestCase):

    def setUp(self):
        self.lst = ['a', [1, 2], 100]
        self.copy = reverse(self.lst)

    def test_reverse(self):
        copy_reversed = self.copy[::-1]
        self.assertListEqual(self.lst, copy_reversed)

    def test_deepcopy(self):
        self.assertFalse(self.lst[1] is self.copy[1])


if __name__ == '__main__':
    unittest.main()
